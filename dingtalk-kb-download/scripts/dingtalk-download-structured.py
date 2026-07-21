#!/usr/bin/env python3
"""
钉钉知识库下载工具 - 递归下载版
自动递归下载所有嵌套文件夹及其内容，保持完整文件夹结构
"""

import asyncio
import json
import re
from pathlib import Path
from playwright.async_api import async_playwright, Page
import httpx

class DingTalkStructuredDownloader:
    def __init__(self, output_dir: str = "downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.downloaded_folders = set()  # 已下载的文件夹UUID
        self.page = None
        self.context = None
        # 统计信息
        self.stats = {
            'folders': 0,
            'files': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0
        }
        
    def sanitize_filename(self, filename: str) -> str:
        """清理文件名中的非法字符"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename
    
    async def get_breadcrumb_path(self) -> list:
        """获取面包屑导航路径，返回文件夹名称列表"""
        try:
            # 尝试从面包屑导航获取路径
            breadcrumb_items = await self.page.evaluate('''
                () => {
                    const items = [];
                    
                    // 尝试多种可能的面包屑选择器
                    const selectors = [
                        '.breadcrumb-item',
                        '.crumb-item',
                        '[class*="breadcrumb"] [class*="item"]',
                        '.folder-breadcrumb span',
                        'nav[aria-label="breadcrumb"] li',
                    ];
                    
                    for (const selector of selectors) {
                        const elements = document.querySelectorAll(selector);
                        if (elements.length > 0) {
                            elements.forEach(el => {
                                const text = el.textContent.trim();
                                if (text && text !== '/' && text !== '>') {
                                    items.push(text);
                                }
                            });
                            break;
                        }
                    }
                    
                    // 如果面包屑获取失败，尝试从页面标题获取
                    if (items.length === 0) {
                        const title = document.querySelector('h1, .page-title, .folder-title');
                        if (title) {
                            items.push(title.textContent.trim());
                        }
                    }
                    
                    return items;
                }
            ''')
            
            return breadcrumb_items
        except Exception as e:
            print(f"   ⚠️ 获取面包屑失败: {e}")
            return []
    
    async def get_current_folder_uuid(self) -> str:
        """获取当前文件夹的UUID"""
        # 从URL中提取
        url = self.page.url
        match = re.search(r'/nodes/([a-zA-Z0-9]+)', url)
        if match:
            return match.group(1)
        
        # 尝试从页面JavaScript获取
        try:
            uuid = await self.page.evaluate('''
                () => {
                    return window.__dentryUuid || 
                           window.currentDentryUuid ||
                           document.querySelector('[data-dentry-uuid]')?.getAttribute('data-dentry-uuid') ||
                           null;
                }
            ''')
            if uuid:
                return uuid
        except:
            pass
        
        return None
    
    async def get_file_list(self, folder_uuid: str) -> list:
        """通过API获取文件夹内容列表"""
        try:
            files_data = await self.page.evaluate('''
                async (folderUuid) => {
                    try {
                        const response = await fetch(`/box/api/v2/dentry/list?dentryUuid=${folderUuid}&orderBy=NAME&order=ASC`, {
                            method: 'GET',
                            headers: {
                                'Accept': 'application/json',
                            },
                            credentials: 'include'
                        });
                        const data = await response.json();
                        return data;
                    } catch (e) {
                        return { error: e.message };
                    }
                }
            ''', folder_uuid)
            
            if 'error' in files_data:
                print(f"     ✗ 获取文件列表失败: {files_data['error']}")
                return []
            
            if not files_data.get('isSuccess'):
                print(f"     ✗ API返回错误: {files_data}")
                return []
            
            return files_data.get('data', {}).get('children', [])
            
        except Exception as e:
            print(f"     ✗ 获取文件列表异常: {e}")
            return []

    async def download_folder_recursive(self, folder_uuid: str, folder_path: Path, depth: int = 0):
        """递归下载文件夹及其所有子文件夹"""
        if folder_uuid in self.downloaded_folders:
            indent = "  " * depth
            print(f"{indent}⏭️  已下载过此文件夹，跳过")
            return
        
        indent = "  " * depth
        self.stats['folders'] += 1
        
        print(f"\n{indent}📁 [{depth+1}级] {folder_path.name}/")
        
        # 创建文件夹
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # 获取文件列表
        children = await self.get_file_list(folder_uuid)
        
        if not children:
            print(f"{indent}  (空文件夹)")
            self.downloaded_folders.add(folder_uuid)
            return
        
        print(f"{indent}  找到 {len(children)} 个项目")
        
        # 分离文件夹和文件
        folders = [c for c in children if c.get('dentryType') == 'folder']
        files = [c for c in children if c.get('dentryType') != 'folder']
        
        # 先下载文件
        for i, child in enumerate(files, 1):
            name = child.get('name', 'unknown')
            dentry_uuid = child.get('dentryUuid', '')
            
            print(f"{indent}  [{i}/{len(files)}] 📄 {name}")
            self.stats['files'] += 1
            
            success = await self.trigger_file_download(dentry_uuid, name, folder_path)
            if success:
                self.stats['success'] += 1
            else:
                self.stats['failed'] += 1
            
            await asyncio.sleep(0.5)  # 节流
        
        # 递归下载子文件夹
        for i, child in enumerate(folders, 1):
            name = child.get('name', 'unknown')
            dentry_uuid = child.get('dentryUuid', '')
            
            safe_name = self.sanitize_filename(name)
            sub_folder_path = folder_path / safe_name
            
            print(f"{indent}  📂 进入子文件夹: {name}")
            
            await self.download_folder_recursive(dentry_uuid, sub_folder_path, depth + 1)
            
            await asyncio.sleep(1)  # 子文件夹间隔
        
        self.downloaded_folders.add(folder_uuid)
        print(f"{indent}✓ 文件夹完成: {folder_path.name}")

    async def download_folder_content(self, folder_uuid: str, folder_path: Path):
        """下载文件夹内容到指定路径（递归版入口）"""
        await self.download_folder_recursive(folder_uuid, folder_path, depth=0)
    
    async def trigger_file_download(self, dentry_uuid: str, file_name: str, save_path: Path) -> bool:
        """触发文件下载，返回是否成功"""
        final_path = save_path / self.sanitize_filename(file_name)
        
        # 增量检查：已存在则跳过
        if final_path.exists():
            print(f"      ⏭️ 已存在，跳过")
            self.stats['skipped'] += 1
            return True
        
        try:
            # 使用浏览器的下载功能
            async with self.page.expect_download(timeout=60000) as download_info:
                await self.page.evaluate(f'''
                    () => {{
                        const link = document.createElement('a');
                        link.href = '/box/api/v2/file/download?dentryUuid={dentry_uuid}';
                        link.download = '{file_name}';
                        link.click();
                    }}
                ''')
            
            download = await download_info.value
            await download.save_as(final_path)
            print(f"      ✓ 已保存: {final_path.name}")
            return True
                
        except Exception as e:
            print(f"      ✗ 下载异常: {e}")
            return False
    
    async def monitor_navigation(self):
        """监听用户导航"""
        last_uuid = None
        
        while True:
            await asyncio.sleep(2)
            
            try:
                current_uuid = await self.get_current_folder_uuid()
                
                if current_uuid and current_uuid != last_uuid:
                    print(f"\n{'='*60}")
                    print(f"🔍 检测到新文件夹: {current_uuid}")
                    
                    # 获取面包屑路径
                    breadcrumb = await self.get_breadcrumb_path()
                    print(f"   路径: {' / '.join(breadcrumb) if breadcrumb else '未知'}")
                    print(f"{'='*60}")
                    
                    # 构建本地文件夹路径
                    if breadcrumb:
                        folder_path = self.output_dir
                        for folder_name in breadcrumb:
                            safe_name = self.sanitize_filename(folder_name)
                            folder_path = folder_path / safe_name
                    else:
                        folder_path = self.output_dir / current_uuid
                    
                    # 递归下载当前文件夹及所有子文件夹
                    await self.download_folder_recursive(current_uuid, folder_path)
                    
                    last_uuid = current_uuid
                    
                    # 显示当前统计
                    self._print_stats()
                    
            except Exception as e:
                print(f"⚠️  监听异常: {e}")

    def _print_stats(self):
        """打印统计信息"""
        print(f"\n📊 当前统计:")
        print(f"   文件夹: {self.stats['folders']} 个")
        print(f"   文件总数: {self.stats['files']} 个")
        print(f"   成功: {self.stats['success']}")
        print(f"   失败: {self.stats['failed']}")
        print(f"   跳过(已存在): {self.stats['skipped']}")
    
    async def run(self):
        """主流程"""
        async with async_playwright() as p:
            print("=" * 60)
            print("钉钉知识库下载工具 - 递归下载版")
            print("=" * 60)
            print("\n📖 使用说明：")
            print("1. 在打开的浏览器中扫码登录钉钉")
            print("2. 导航到要下载的知识库文件夹")
            print("3. 工具会自动递归下载该文件夹及所有子文件夹")
            print("4. 已下载的文件会自动跳过（支持增量下载）")
            print("5. 按 Ctrl+C 停止下载")
            print("=" * 60)
            print("\n💡 提示：")
            print("   - 点击进入任意文件夹，工具会自动下载其所有内容")
            print("   - 支持多层嵌套文件夹结构")
            print("   - 大文件夹可能需要较长时间，请耐心等待")
            print("=" * 60)
            
            # 启动浏览器
            browser = await p.chromium.launch(headless=False)
            self.context = await browser.new_context(accept_downloads=True)
            self.page = await self.context.new_page()
            
            # 导航到钉钉文档
            print("\n🌐 正在打开钉钉文档...")
            try:
                await self.page.goto("https://alidocs.dingtalk.com", timeout=60000)
            except:
                pass
            
            print("\n✓ 浏览器已打开")
            print("   请登录并点击进入要下载的知识库文件夹\n")
            
            # 开始监听用户导航
            try:
                await self.monitor_navigation()
            except KeyboardInterrupt:
                print("\n\n⏹️  用户停止下载")
            finally:
                # 最终统计
                print("\n" + "=" * 60)
                print("📥 下载完成统计")
                print("=" * 60)
                print(f"   处理文件夹: {self.stats['folders']} 个")
                print(f"   文件总数: {self.stats['files']} 个")
                print(f"   下载成功: {self.stats['success']}")
                print(f"   下载失败: {self.stats['failed']}")
                print(f"   跳过(已存在): {self.stats['skipped']}")
                print("=" * 60)
                print(f"\n📁 文件保存在: {self.output_dir.absolute()}")
                
                await browser.close()

async def main():
    downloader = DingTalkStructuredDownloader(output_dir="D:\\钉钉知识库备份")
    await downloader.run()

if __name__ == "__main__":
    asyncio.run(main())
