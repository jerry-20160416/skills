# 一、编程规约
## (一) 命名风格
1.【强制】所有编程相关的命名均不能以下划线或美元符号开始，也不能以下划线或美元符号结束。
反例：_name / __name / $Object / name_ / name$ / Object$
2.【强制】所有编程相关的命名严禁使用拼音与英文混合的方式，更不允许直接使用中文的方式。
说明：正确的英文拼写和语法可以让阅读者易于理解，避免歧义。注意，即使纯拼音命名方式也要避免采用。
正例：ali / alibaba / taobao / kaikeba / aliyun / youku / hangzhou 等国际通用的名称，可视同英文。
反例：DaZhePromotion【打折】/ getPingfenByName()【评分】 / String fw【福娃】/ int 变量名 = 3
3.【强制】代码和注释中都要避免使用任何人类语言中的种族歧视性或侮辱性词语。
正例：blockList / allowList / secondary
反例：blackList / whiteList / slave / SB / WTF
4.【强制】类名使用UpperCamelCase 风格，以下情形例外：DO / PO / DTO / BO / VO / UID 等。
正例：ForceCode / UserDO / HtmlDTO / XmlService / TcpUdpDeal / TaPromotion
反例：forcecode / UserDo / HTMLDto / XMLService / TCPUDPDeal / TAPromotion
5.【强制】方法名、参数名、成员变量、局部变量都统一使用lowerCamelCase 风格。
正例：localValue / getHttpMessage() / inputUserId
6.【强制】常量命名应该全部大写，单词间用下划线隔开，力求语义表达完整清楚，不要嫌名字长。
正例：MAX_STOCK_COUNT / CACHE_EXPIRED_TIME
反例：MAX_COUNT / EXPIRED_TIME
7.【强制】抽象类命名使用Abstract 或Base 开头；异常类命名使用Exception 结尾，测试类命名以它要
测试的类的名称开始，以Test 结尾。
8.【强制】类型与中括号紧挨相连来定义数组。
正例：定义整形数组int[] arrayDemo。
反例：在main 参数中，使用String args[] 来定义。
9.【强制】POJO 类中的任何布尔类型的变量，都不要加is 前缀，否则部分框架解析会引起序列化错误。
说明：本文MySQL 规约中的建表约定第1 条，表达是与否的变量采用is_xxx 的命名方式，所以需要在<resultMap>
设置从is_xxx 到xxx 的映射关系。
反例：定义为布尔类型Boolean isDeleted 的字段，它的getter 方法也是isDeleted()，部分框架在反向解析时，“误以
为”对应的字段名称是deleted，导致字段获取不到，得到意料之外的结果或抛出异常。
10.【强制】包名统一使用小写，点分隔符之间有且仅有一个自然语义的英语单词。包名统一使用单数形
式，但是类名如果有复数含义，类名可以使用复数形式。
正例：应用工具类包名为com.alibaba.ei.kunlun.aap.util；类名为MessageUtils（此规则参考spring 的框架结构）。
11.【强制】避免在子父类的成员变量之间、或者不同代码块的局部变量之间采用完全相同的命名，使可理
解性降低。
说明：子类、父类成员变量名相同，即使是public 也是能够通过编译，而局部变量在同一方法内的不同代码块中同名
也是合法的，但是要避免使用。对于非setter / getter 的参数名称也要避免与成员变量名称相同。
反例：
public class ConfusingName {
protected int stock;
protected String alibaba;
// 非setter/getter 的参数名称，不允许与本类成员变量同名
public void access(String alibaba) {
if (condition) {
final int money = 666;
// ...
}
for (int i = 0; i < 10; i++) {
// 在同一方法体中，不允许与其它代码块中的money 命名相同
final int money = 15978;
// ...
}
}
}
class Son extends ConfusingName {
// 不允许与父类的成员变量名称相同
private int stock;
}
12.【强制】杜绝完全不规范的英文缩写，避免望文不知义。
反例：AbstractClass“缩写”成AbsClass；condition“缩写”成condi；Function“缩写”成Fu，此类随意缩写
严重降低了代码的可阅读性。
13.【推荐】为了达到代码自解释的目标，任何自定义编程元素在命名时，使用完整的单词组合来表达。
正例：在JDK 中，对某个对象引用的volatile 字段进行原子更新的类名为AtomicReferenceFieldUpdater。
反例：常见的方法内变量为int a; 的定义方式。
14.【推荐】在常量与变量命名时，表示类型的名词放在词尾，以提升辨识度。
正例：startTime / workQueue / nameList / TERMINATED_THREAD_COUNT
反例：startedAt / QueueOfWork / listName / COUNT_TERMINATED_THREAD
15.【推荐】如果模块、接口、类、方法使用了设计模式，在命名时要体现出具体模式。
说明：将设计模式体现在名字中，有利于阅读者快速理解架构设计思想。
正例： public class OrderFactory;
public class LoginProxy;
public class ResourceObserver;
16.【推荐】接口类中的方法和属性不要加任何修饰符号（public 也不要加），保持代码的简洁性，并加上
有效的Javadoc 注释。尽量不要在接口里定义常量，如果一定要定义，最好确定该常量与接口的方法
相关，并且是整个应用的基础常量。
正例：接口方法签名void commit();
接口基础常量String COMPANY = "alibaba";
反例：接口方法定义public abstract void commit();
说明：JDK8 中接口允许有默认实现，那么这个default 方法，是对所有实现类都有价值的默认实现。
17.接口和实现类的命名有两套规则：
1）【强制】对于Service 和DAO 类，基于SOA 的理念，暴露出来的服务一定是接口，内部的实现类用Impl 的后缀
与接口区别。
正例：CacheServiceImpl 实现CacheService 接口。
2）【推荐】如果是形容能力的接口名称，取对应的形容词为接口名（通常是 –able 结尾的形容词）。
正例：AbstractTranslator 实现Translatable。
18.【参考】枚举类名带上Enum 后缀，枚举成员名称需要全大写，单词间用下划线隔开。
说明：枚举其实就是特殊的常量类，且构造方法被默认强制是私有。
正例：枚举名字为ProcessStatusEnum 的成员名称：SUCCESS / UNKNOWN_REASON
19.【参考】各层命名规约：
A）Service / DAO 层方法命名规约：
1）获取单个对象的方法用get 做前缀。
2）获取多个对象的方法用list 做前缀，复数结尾，如：listObjects
3）获取统计值的方法用count 做前缀。
4）插入的方法用save / insert 做前缀。
5）删除的方法用remove / delete 做前缀。
6）修改的方法用update 做前缀。
B）领域模型命名规约：
1）数据对象：xxxDO，xxx 即为数据表名。
2）数据传输对象：xxxDTO，xxx 为业务领域相关的名称。
3）展示对象：xxxVO，xxx 一般为网页名称。
4）POJO 是DO / DTO / BO / VO 的统称，禁止命名成xxxPOJO。
## (二) 常量定义
1.【强制】不允许任何魔法值（即未经预先定义的常量）直接出现在代码中。
反例：
//  开发者A 定义了缓存的key。
String key = "Id#taobao_" + tradeId;
cache.put(key, value);
// 开发者B 使用缓存时直接复制少了下划线，即key 是"Id#taobao" + tradeId，导致出现故障。
String key = "Id#taobao" + tradeId;
cache.get(key);
2.【强制】long 或Long 赋值时，数值后使用大写L，不能是小写l，小写容易跟数字混淆，造成误解。
说明：public static final Long NUM = 2l; 写的是数字的21，还是Long 型的2？
3.【强制】浮点数类型的数值后缀统一为大写的D 或F。
正例：public static final double HEIGHT = 175.5D;
public static final float WEIGHT = 150.3F;
4.【推荐】不要使用一个常量类维护所有常量，要按常量功能进行归类，分开维护。
说明：大而全的常量类，杂乱无章，使用查找功能才能定位到要修改的常量，不利于理解，也不利于维护。
正例：缓存相关常量放在类CacheConsts 下；系统配置相关常量放在类SystemConfigConsts 下。
5.【推荐】常量的复用层次有五层：跨应用共享常量、应用内共享常量、子工程内共享常量、包内共享常
量、类内共享常量。
1）跨应用共享常量：放置在二方库中，通常是client.jar 中的constant 目录下。
2）应用内共享常量：放置在一方库中，通常是子模块中的constant 目录下。
反例：易懂常量也要统一定义成应用内共享常量，两个程序员在两个类中分别定义了表示“是”的常量：
类A 中：public static final String YES = "yes";
类B 中：public static final String YES = "y";
A.YES.equals(B.YES)，预期是true，但实际返回为false，导致线上问题。
3）子工程内部共享常量：即在当前子工程的constant 目录下。
4）包内共享常量：即在当前包下单独的constant 目录下。
5）类内共享常量：直接在类内部private static final 定义。
6.【推荐】如果变量值仅在一个固定范围内变化用enum 类型来定义。
说明：如果存在名称之外的延伸属性应使用enum 类型，下面正例中的数字就是延伸信息，表示一年中的第几个季节。
正例：
public enum SeasonEnum {
SPRING(1), SUMMER(2), AUTUMN(3), WINTER(4);
private int seq;
SeasonEnum(int seq) {
this.seq = seq;
}
public int getSeq() {
return seq;
}
}
## (三) 代码格式
1.【强制】如果大括号内为空，简洁地写成{}即可，大括号中间无需换行和空格；如果是非空代码块，则：
1）左大括号前不换行。
2）左大括号后换行。
3）右大括号前换行。
4）右大括号后还有else 等代码则不换行；表示终止的右大括号后必须换行。
2.【强制】左小括号和右边相邻字符之间不需要空格；右小括号和左边相邻字符之间也不需要空格；而左大
括号前需要加空格。详见第5 条下方正例提示。
反例：if(空格 a == b 空格)
3.【强制】if / for / while / switch / do 等保留字与左右括号之间都必须加空格。
4.【强制】任何二目、三目运算符的左右两边都需要加一个空格。
说明：包括赋值运算符 =、逻辑运算符 &&、加减乘除符号等。
5.【强制】采用4 个空格缩进，禁止使用Tab 字符。
说明：如使用Tab 缩进，必须设置1 个Tab 为4 个空格。IDEA 设置Tab 为4 个空格时，请勿勾选Use tab character；
而在Eclipse 中，找到tab policy 设置为Spaces only，Tab size：4，最后必须勾选insert spaces for tabs
正例：（涉及上述中的1-5 点）
public static void main(String[] args) {
// 缩进4 个空格
String say = "hello";
// 运算符的左右必须有一个空格
int flag = 0;
// 关键词if 与括号之间必须有一个空格，括号内的f 与左括号，0 与右括号不需要空格
if (flag == 0) {
System.out.println(say);
}
// 左大括号前加空格且不换行；左大括号后换行
if (flag == 1) {
System.out.println("world");
// 右大括号前换行，右大括号后有else，不用换行
} else {
System.out.println("ok");
// 在右大括号后直接结束，则必须换行
}
}
6.【强制】注释的双斜线与注释内容之间有且仅有一个空格。
正例：
// 这是示例注释，请注意在双斜线之后有一个空格
String commentString = new String("demo");
7.【强制】在进行类型强制转换时，右括号与强制转换值之间不需要任何空格隔开。
正例：
double first = 3.2D;
int second = (int)first + 2;
8.【强制】单行字符数限制不超过120 个，超出需要换行，换行时遵循如下原则：
1）第二行相对第一行缩进4 个空格，从第三行开始，不再继续缩进，参考示例。
2）运算符与下文一起换行。
3）方法调用的点符号与下文一起换行。
4）方法调用中的多个参数需要换行时，在逗号后进行。
5）在括号前不要换行，见反例。
正例：
StringBuilder builder = new StringBuilder();
// 超过120 个字符的情况下，换行缩进4 个空格，并且方法前的点号一起换行
builder.append("yang").append("hao")...
.append("chen")...
.append("chen")...
.append("chen");
反例：
StringBuilder builder = new StringBuilder();
// 超过120 个字符的情况下，不要在括号前换行
builder.append("you").append("are")...append
("lucky");
// 参数很多的方法调用可能超过120 个字符，逗号后才是换行处
method(args1, args2, args3, ...
, argsX);
9.【强制】方法参数在定义和传入时，多个参数逗号后面必须加空格。
正例：下例中实参的args1 逗号后边必须要有一个空格。
method(args1, args2, args3);
10.【强制】IDE 的text file encoding 设置为UTF-8；IDE 中文件的换行符使用Unix 格式，不要使用
Windows 格式。
11.【推荐】单个方法的总行数不超过80 行。
说明：除注释之外的方法签名、左右大括号、方法内代码、空行、回车及任何不可见字符的总行数不超过80 行。
正例：代码逻辑分清红花和绿叶，个性和共性，绿叶逻辑单独出来成为额外方法，使主干代码更加晰；共性逻辑抽取
成为共性方法，便于复用和维护。
12.【推荐】没有必要增加若干空格来使变量的赋值等号与上一行对应位置的等号对齐。
正例：
int one = 1;
long two = 2L;
float three = 3F;
StringBuilder builder = new StringBuilder();
说明：增加builder 这个变量，如果需要对齐，则给one、two、three 都要增加几个空格，在变量比较多的情况下，是
非常累赘的事情。
13.【推荐】不同逻辑、不同语义、不同业务的代码之间插入一个空行，分隔开来以提升可读性。
说明：任何情形，没有必要插入多个空行进行隔开。
## (四) OOP 规约
1.【强制】避免通过一个类的对象引用访问此类的静态变量或静态方法，无谓增加编译器解析成本，直接用
类名来访问即可。
2.【强制】所有的覆写方法，必须加 @Override 注解。
说明：getObject() 与get0bject() 的问题。一个是字母的O，一个是数字的0，加 @Override 可以准确判断是否覆盖
成功。另外，如果在抽象类中对方法签名进行修改，其实现类会马上编译报错。
3.【强制】相同参数类型，相同业务含义，才可以使用的可变参数，参数类型避免定义为Object。
说明：可变参数必须放置在参数列表的最后。（建议开发者尽量不用可变参数编程）
正例：public List<User> listUsers(String type, Long... ids) {...}
4.【强制】外部正在调用的接口或者二方库依赖的接口，不允许修改方法签名，避免对接口调用方产生影
响。接口过时必须加 @Deprecated 注解，并清晰地说明采用的新接口或者新服务是什么。
5.【强制】不能使用过时的类或方法。
说明：java.net.URLDecoder 中的方法decode(String encodeStr) 这个方法已经过时，应该使用双参数
decode(String source, String encode)。接口提供方既然明确是过时接口，那么有义务同时提供新的接口；作为调用
方来说，有义务去考证过时方法的新实现是什么。
6.【强制】Object 的equals 方法容易抛空指针异常，应使用常量或确定有值的对象来调用equals。
正例："test".equals(param);
反例：param.equals("test");
说明：推荐使用JDK7 引入的工具类java.util.Objects#equals(Object a, Object b)
7.【强制】所有整型包装类对象之间值的比较，全部使用equals 方法比较。
说明：对于Integer var = ? 在 -128 至127 之间的赋值，Integer 对象是在IntegerCache.cache 产生，会复用已有对
象，这个区间内的Integer 值可以直接使用 == 进行判断，但是这个区间之外的所有数据，都会在堆上产生，并不会复
用已有对象，这是一个大坑，推荐使用equals 方法进行判断。
8.【强制】任何货币金额，均以最小货币单位且为整型类型进行存储。
9.【强制】浮点数之间的等值判断，基本数据类型不能使用 == 进行比较，包装数据类型不能使用equals
进行判断。
说明：浮点数采用“尾数+阶码”的编码方式，类似于科学计数法的“有效数字+指数”的表示方式。二进制无法精确表
示大部分的十进制小数，具体原理参考《码出高效》。
反例：
float a = 1.0F - 0.9F;
float b = 0.9F - 0.8F;
if (a == b) {
// 预期进入此代码块，执行其它业务逻辑
// 但事实上a == b 的结果为false
}
Float x = Float.valueOf(a);
Float y = Float.valueOf(b);
if (x.equals(y)) {
// 预期进入此代码块，执行其它业务逻辑
// 但事实上equals 的结果为false
}
正例：
(1)指定一个误差范围，两个浮点数的差值在此范围之内，则认为是相等的。
float a = 1.0F - 0.9F;
float b = 0.9F - 0.8F;
float diff = 1e-6F;
if (Math.abs(a - b) < diff) {
System.out.println("true");
}
(2)使用BigDecimal 来定义值，再进行浮点数的运算操作。
BigDecimal a = new BigDecimal("1.0");
BigDecimal b = new BigDecimal("0.9");
BigDecimal c = new BigDecimal("0.8");
BigDecimal x = a.subtract(b);
BigDecimal y = b.subtract(c);
if (x.compareTo(y) == 0) {
System.out.println("true");
}
10.【强制】BigDecimal 的等值比较应使用compareTo() 方法，而不是equals() 方法。
说明：equals() 方法会比较值和精度（1.0 与 1.00 返回结果为 false），而compareTo() 则会忽略精度。
11.【强制】定义数据对象DO 类时，属性类型要与数据库字段类型相匹配。
正例：数据库字段的bigint 必须与类属性的Long 类型相对应。
反例：某业务的数据库表id 字段定义类型为bigint unsigned，实际类对象属性为Integer，随着id 越来越大，
超过Integer 的表示范围而溢出成为负数，此时数据库id 不支持存入负数抛出异常产生线上故障。
12.【强制】禁止使用构造方法BigDecimal(double) 的方式把double 值转化为BigDecimal 对象。
说明：BigDecimal(double) 存在精度损失风险，在精确计算或值比较的场景中可能会导致业务逻辑异常。 如：
BigDecimal g = new BigDecimal(0.1F)；实际的存储值为：0.100000001490116119384765625
正例：优先推荐入参为String 的构造方法，或使用BigDecimal 的valueOf 方法，此方法内部其实执行了Double 的
toString，而Double 的toString 按double 的实际能表达的精度对尾数进行了截断。
BigDecimal recommend1 = new BigDecimal("0.1");
BigDecimal recommend2 = BigDecimal.valueOf(0.1);
13.关于基本数据类型与包装数据类型的使用标准如下：
1）【强制】所有的POJO 类属性必须使用包装数据类型。
2）【强制】RPC 方法的返回值和参数必须使用包装数据类型。
3）【推荐】所有的局部变量使用基本数据类型。
说明：POJO 类属性没有初值是提醒使用者在需要使用时，必须自己显式地进行赋值，任何NPE 问题，或者入库检查，
都由使用者来保证。
正例：数据库的查询结果可能是null，因为自动拆箱，用基本数据类型接收有NPE 风险。
反例：某业务的交易报表上显示成交总额涨跌情况，即正负x%，x 为基本数据类型，调用的RPC 服务，调用不成功时，
返回的是默认值，页面显示为0%，这是不合理的，应该显示成中划线-。所以包装数据类型的null 值，能够表示额外的
信息，如：远程调用失败，异常退出。
14.【强制】定义DO / PO / DTO / VO 等POJO 类时，不要设定任何属性默认值。
反例：某业务的DO 的createTime 默认值为new Date()；但是这个属性在数据提取时并没有置入具体值，在更新其
它字段时又附带更新了此字段，导致创建时间被修改成当前时间。
15.【强制】序列化类新增属性时，请不要修改serialVersionUID 字段，避免反序列失败；如果完全不兼
容升级，避免反序列化混乱，那么请修改serialVersionUID 值。
说明：注意serialVersionUID 不一致会抛出序列化运行时异常。
16.【强制】构造方法里面禁止加入任何业务逻辑，如果有初始化逻辑，请放在init 方法中。
17.【强制】POJO 类必须写toString 方法。使用IDE 中的工具source > generate toString 时，如果继
承了另一个POJO 类，注意在前面加一下super.toString()。
说明：在方法执行抛出异常时，可以直接调用POJO 的toString() 方法打印其属性值，便于排查问题。
18.【强制】禁止在POJO 类中，同时存在对应属性xxx 的isXxx() 和getXxx() 方法。
说明：框架在调用属性xxx 的提取方法时，并不能确定哪个方法一定是被优先调用到，神坑之一。
19.【推荐】使用索引访问用String 的split 方法得到的数组时，需做最后一个分隔符后有无内容的检查，
否则会有抛IndexOutOfBoundsException 的风险。
说明：
String str = "a,b,c,,";
String[] ary = str.split(",");
// 预期大于3，结果等于3
System.out.println(ary.length);
20.【推荐】当一个类有多个构造方法，或者多个同名方法，这些方法应该按顺序放置在一起，便于阅读，
此条规则优先于下一条。
正例：
public int method(int param);
protected double method(int param1, int param2);
private void method();
21.【推荐】类内方法定义的顺序依次是：公有方法或保护方法 > 私有方法 > getter / setter 方法。
说明：公有方法是类的调用者和维护者最关心的方法，首屏展示最好；保护方法虽然只是子类关心，也可能是“模板设
计模式”下的核心方法；而私有方法外部一般不需要特别关心，是一个黑盒实现；因为承载的信息价值较低，所有
Service 和DAO 的getter / setter 方法放在类体最后。
22.【推荐】setter 方法中，参数名称与类成员变量名称一致，this.成员名=参数名。在getter / setter 方
法中，不要增加业务逻辑，增加排查问题的难度。
反例：
public Integer getData() {
if (condition) {
return this.data + 100;
} else {
return this.data - 100;
}
}
23.【推荐】循环体内，字符串的连接方式，使用StringBuilder 的append 方法进行扩展。
反例：
String str = "start";
for (int i = 0; i < 100; i++) {
str = str + "hello";
}
说明：反编译出的字节码文件显示每次循环都会new 出一个StringBuilder 对象，然后进行append 操作，最后通过
toString() 返回String 对象，造成内存资源浪费。
24.【推荐】final 可以声明类、成员变量、方法、以及本地变量，下列情况使用final 关键字：
1）不允许被继承的类，如：String 类。
2）不允许修改引用的域对象，如：POJO 类的域变量。
3）不允许被覆写的方法，如：POJO 类的setter 方法。
4）不允许运行过程中重新赋值的局部变量。
5）避免上下文重复使用一个变量，使用final 关键字可以强制重新定义一个变量，方便更好地进行重构。
25.【推荐】慎用Object 的clone 方法来拷贝对象。
说明：对象clone 方法默认是浅拷贝，若想实现深拷贝需覆写clone 方法实现域对象的深度遍历式拷贝。
26.【推荐】类成员与方法访问控制从严：
1）如果不允许外部直接通过new 来创建对象，那么构造方法必须是private。
2）工具类不允许有public 或default 构造方法。
3）类非static 成员变量并且与子类共享，必须是protected。
4）类非static 成员变量并且仅在本类使用，必须是private。
5）类static 成员变量如果仅在本类使用，必须是private。
6）若是static 成员变量，考虑是否为final。
7）类成员方法只供类内部调用，必须是private。
8）类成员方法只对继承类公开，那么限制为protected。
说明：任何类、方法、参数、变量，严控访问范围。过于宽泛的访问范围，不利于模块解耦。思考：如果是一个
private 的方法，想删除就删除，可是一个public 的service 成员方法或成员变量，删除一下，不得手心冒点汗吗？
变量像自己的小孩，尽量在自己的视线内，变量作用域太大，无限制的到处跑，那么你会担心的。
## (五) 日期时间
1.【强制】日期格式化时，传入pattern 中表示年份统一使用小写的y。
说明：日期格式化时，yyyy 表示当天所在的年，而大写的YYYY 代表是week in which year（JDK7 之后引入的概念），
意思是当天所在的周属于的年份，一周从周日开始，周六结束，只要本周跨年，返回的YYYY 就是下一年。
正例：表示日期和时间的格式如下所示：
new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
反例：某程序员因使用YYYY/MM/dd 进行日期格式化，2017/12/31 执行结果为2018/12/31，造成线上故障。
2.【强制】在日期格式中分清楚大写的M 和小写的m，大写的H 和小写的h 分别指代的意义。
说明：日期格式中的这两对字母表意如下：
1）表示月份是大写的M
2）表示分钟则是小写的m
3）24 小时制的是大写的H
4）12 小时制的则是小写的h
3.【强制】获取当前毫秒数：System.currentTimeMillis()；而不是new Date().getTime()。
说明：获取纳秒级时间，则使用System.nanoTime 的方式。在JDK8 中，针对统计时间等场景，推荐使用Instant 类。
4.【强制】不允许在程序任何地方中使用：1）java.sql.Date  2）java.sql.Time  3）java.sql.Timestamp。
说明：第1 个不记录时间，getHours() 抛出异常；第2 个不记录日期，getYear() 抛出异常；第3 个在构造方法
super((time / 1000) * 1000)，在Timestamp 属性fastTime 和nanos 分别存储秒和纳秒信息。
反例：java.util.Date.after(Date) 进行时间比较时，当入参是java.sql.Timestamp 时，会触发JDK BUG（JDK9 已修
复），可能导致比较时的意外结果。
5.【强制】禁止在程序中写死一年为365 天，避免在公历闰年时出现日期转换错误或程序逻辑错误。
正例：
// 获取今年的天数
int daysOfThisYear = LocalDate.now().lengthOfYear();
// 获取指定某年的天数
LocalDate.of(2011, 1, 1).lengthOfYear();
反例：
// 第一种情况：在闰年366 天时，出现数组越界异常
int[] dayArray = new int[365];
// 第二种情况：一年有效期的会员制，2020 年1 月26 日注册，硬编码365 返回的却是2021 年1 月25 日
Calendar calendar = Calendar.getInstance();
calendar.set(2020, 1, 26);
calendar.add(Calendar.DATE, 365);
6.【推荐】避免公历闰年2 月问题。闰年的2 月份有29 天，一年后的那一天不可能是2 月29 日。
7.【推荐】使用枚举值来指代月份。如果使用数字，注意Date，Calendar 等日期相关类的月份month 取
值范围从0 到11 之间。
说明：参考JDK 原生注释，Month value is 0-based. e.g., 0 for January.
正例：Calendar.JANUARY，Calendar.FEBRUARY，Calendar.MARCH 等来指代相应月份来进行传参或比较。
## (六) 集合处理
1.【强制】关于hashCode 和equals 的处理，遵循如下规则：
1）只要覆写equals，就必须覆写hashCode。
2）因为Set 存储的是不重复的对象，依据hashCode 和equals 进行判断，所以Set 存储的对象必须覆写这两种方法。
3）如果自定义对象作为Map 的键，那么必须覆写hashCode 和equals。
说明：String 因为覆写了hashCode 和equals 方法，所以可以愉快地将String 对象作为key 来使用。
2.【强制】判断所有集合内部的元素是否为空，使用isEmpty() 方法，而不是size() == 0 的方式。
说明：在某些集合中，前者的时间复杂度为O(1)，而且可读性更好。
正例：
Map<String, Object> map = new HashMap<>(16);
if (map.isEmpty()) {
System.out.println("no element in this map.");
}
3.【强制】在使用java.util.stream.Collectors 类的toMap() 方法转为Map 集合时，一定要使用参数类型
为BinaryOperator，参数名为mergeFunction 的方法，否则当出现相同key 时会抛出
IllegalStateException 异常。
说明：参数mergeFunction 的作用是当出现key 重复时，自定义对value 的处理策略。
正例：
List<Pair<String, Double>> pairArrayList = new ArrayList<>(3);
pairArrayList.add(new Pair<>("version", 12.10));
pairArrayList.add(new Pair<>("version", 12.19));
pairArrayList.add(new Pair<>("version", 6.28));
// 生成的map 集合中只有一个键值对：{version=6.28}
Map<String, Double> map = pairArrayList.stream()
.collect(Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));
反例：
String[] departments = new String[]{"RDC", "RDC", "KKB"};
// 抛出IllegalStateException 异常
Map<Integer, String> map = Arrays.stream(departments)
.collect(Collectors.toMap(String::hashCode, str -> str));
4.【强制】在使用java.util.stream.Collectors 类的toMap() 方法转为Map 集合时，一定要注意当value
为null 时会抛NPE 异常。
说明：在java.util.HashMap 的merge 方法里会进行如下的判断：
if (value == null || remappingFunction == null)
throw new NullPointerException();
反例：
List<Pair<String, Double>> pairArrayList = new ArrayList<>(2);
pairArrayList.add(new Pair<>("version1", 8.3));
pairArrayList.add(new Pair<>("version2", null));
// 抛出NullPointerException 异常
Map<String, Double> map = pairArrayList.stream()
.collect(Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));
5.【强制】ArrayList 的subList 结果不可强转成ArrayList，否则会抛出ClassCastException 异常：
java.util.RandomAccessSubList cannot be cast to java.util.ArrayList。
说明：subList() 返回的是ArrayList 的内部类SubList，并不是ArrayList 本身，而是ArrayList 的一个视图，对于
SubList 的所有操作最终会反映到原列表上。
6.【强制】使用Map 的方法keySet() / values() / entrySet() 返回集合对象时，不可以对其进行添加元素
操作，否则会抛出UnsupportedOperationException 异常。
7.【强制】Collections 类返回的对象，如：emptyList() / singletonList() 等都是immutable list，不可
对其进行添加或者删除元素的操作。
反例：如果查询无结果，返回Collections.emptyList() 空集合对象，调用方一旦在返回的集合中进行了添加元素的操
作，就会触发UnsupportedOperationException 异常。
8.【强制】在subList 场景中，高度注意对父集合元素的增加或删除，均会导致子列表的遍历、增加、删
除产生ConcurrentModificationException 异常。
说明：抽查表明，90% 的程序员对此知识点都有错误的认知。
9.【强制】使用集合转数组的方法，必须使用集合的toArray(T[] array)，传入的是类型完全一致、长度为
0 的空数组。
反例：直接使用toArray 无参方法存在问题，此方法返回值只能是Object[]类，若强转其它类型数组将出现
ClassCastException 错误。
正例：
List<String> list = new ArrayList<>(2);
list.add("guan");
list.add("bao");
String[] array = list.toArray(new String[0]);
说明：使用toArray 带参方法，数组空间大小的length：
1）等于0，动态创建与size 相同的数组，性能最好。
2）大于0 但小于size，重新创建大小等于size 的数组，增加GC 负担。
3）等于size，在高并发情况下，数组创建完成之后，size 正在变大的情况下，负面影响与2 相同。
4）大于size，空间浪费，且在size 处插入null 值，存在NPE 隐患。
10.【强制】使用Collection 接口任何实现类的addAll() 方法时，要对输入的集合参数进行NPE 判断。
说明：在ArrayList#addAll 方法的第一行代码即Object[] a = c.toArray()；其中c 为输入集合参数，如果为null，
则直接抛出异常。
11.【强制】使用工具类Arrays.asList() 把数组转换成集合时，不能使用其修改集合相关的方法，它的add
/ remove / clear 方法会抛出UnsupportedOperationException 异常。
说明：asList 的返回对象是一个Arrays 内部类，并没有实现集合的修改方法。Arrays.asList 体现的是适配器模式，只
是转换接口，后台的数据仍是数组。
String[] str = new String[]{ "yang", "guan", "bao" };
List list = Arrays.asList(str);
第一种情况：list.add("yangguanbao"); 运行时异常。
第二种情况：str[0] = "change"; list 中的元素也会随之修改，反之亦然。
12.【强制】泛型通配符<? extends T>来接收返回的数据，此写法的泛型集合不能使用add 方法，
而<? super T>不能使用get 方法，两者在接口调用赋值的场景中容易出错。
说明：扩展说一下PECS(Producer Extends Consumer Super) 原则，即频繁往外读取内容的，适合用
<? extends T>，经常往里插入的，适合用<? super T>
13.【强制】在无泛型限制定义的集合赋值给泛型限制的集合时，在使用集合元素时，需要进行
instanceof 判断，避免抛出ClassCastException 异常。
说明：毕竟泛型是在JDK5 后才出现，考虑到向前兼容，编译器是允许非泛型集合与泛型集合互相赋值。
反例：
List<String> generics = null;
List notGenerics = new ArrayList(10);
notGenerics.add(new Object());
notGenerics.add(new Integer(1));
generics = notGenerics;
// 此处抛出ClassCastException 异常
String string = generics.get(0);
14.【强制】不要在foreach 循环里进行元素的remove / add 操作。remove 元素请使用iterator 方式，
如果并发操作，需要对iterator 对象加锁。
正例：
List<String> list = new ArrayList<>();
list.add("1");
list.add("2");
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
String item = iterator.next();
if (删除元素的条件) {
iterator.remove();
}
}
反例：
for (String item : list) {
if ("1".equals(item)) {
list.remove(item);
}
}
说明：反例中的执行结果肯定会出乎大家的意料，那么试一下把“1”换成“2”会是同样的结果吗？
15.【强制】在JDK7 版本及以上，Comparator 实现类要满足如下三个条件，不然Arrays.sort，
Collections.sort 会抛IllegalArgumentException 异常。
说明：三个条件如下
1）x，y 的比较结果和y，x 的比较结果相反。
2）x > y，y > z，则x > z。
3）x = y，则x，z 比较结果和y，z 比较结果相同。
反例：下例中没有处理相等的情况，交换两个对象判断结果并不互反，不符合第一个条件，在实际使用中可能会出现异
常。
new Comparator<Student>() {
@Override
public int compare(Student o1, Student o2) {
return o1.getId() > o2.getId() ? 1 : -1;
}
};
16.【推荐】泛型集合使用时，在JDK7 及以上，使用diamond 语法或全省略。
说明：菱形泛型，即diamond，直接使用<>来指代前边已经指定的类型。
正例：
// diamond 方式，即<>
HashMap<String, String> userCache = new HashMap<>(16);
// 全省略方式
ArrayList<User> users = new ArrayList(10);
17.【推荐】集合初始化时，指定集合初始值大小。
说明：HashMap 使用构造方法HashMap(int initialCapacity) 进行初始化时，如果暂时无法确定集合大小，那么指
定默认值（16）即可。
正例：initialCapacity = (需要存储的元素个数 / 负载因子) + 1。注意负载因子（即loaderfactor）默认为0.75，如果
暂时无法确定初始值大小，请设置为16（即默认值）。
反例：HashMap 需要放置1024 个元素，由于没有设置容量初始大小，随着元素增加而被迫不断扩容，resize() 方法
总共会调用8 次，反复重建哈希表和数据迁移。当放置的集合元素个数达千万级时会影响程序性能。
18.【推荐】使用entrySet 遍历Map 类集合KV，而不是keySet 方式进行遍历。
说明：keySet 其实是遍历了2 次，一次是转为Iterator 对象，另一次是从hashMap 中取出key 所对应的value。而
entrySet 只是遍历了一次就把key 和value 都放到了entry 中，效率更高。如果是JDK8，使用Map.forEach 方法。
正例：values() 返回的是V 值集合，是一个list 集合对象；keySet() 返回的是K 值集合，是一个Set 集合对象；
entrySet() 返回的是K-V 值组合的Set 集合。
19.【推荐】高度注意Map 类集合K / V 能不能存储null 值的情况，如下表格：
集合类
Key
Value
Super
说明
Hashtable
不允许为null
不允许为null
Dictionary
线程安全
TreeMap
不允许为null
允许为null
AbstractMap
线程不安全
ConcurrentHashMap
不允许为null
不允许为null
AbstractMap
锁分段技术（JDK8:CAS）
HashMap
允许为null
允许为null
AbstractMap
线程不安全
反例：由于HashMap 的干扰，很多人认为ConcurrentHashMap 是可以置入null 值，而事实上，存储null 值时会抛
出NPE 异常。
20.【参考】合理利用好集合的有序性（sort）和稳定性（order），避免集合的无序性（unsort）和不稳定
性（unorder）带来的负面影响。
说明：有序性是指遍历的结果是按某种比较规则依次排列的，稳定性指集合每次遍历的元素次序是一定的。如：
ArrayList 是order / unsort；HashMap 是unorder / unsort；TreeSet 是order / sort。
21.【参考】利用Set 元素唯一的特性，可以快速对一个集合进行去重操作，避免使用List 的
contains() 进行遍历去重或者判断包含操作。
## (七) 并发处理
1.【强制】获取单例对象需要保证线程安全，其中的方法也要保证线程安全。
说明：资源驱动类、工具类、单例工厂类都需要注意。
2.【强制】创建线程或线程池时请指定有意义的线程名称，方便出错时回溯。
正例：自定义线程工厂，并且根据外部特征进行分组，比如，来自同一机房的调用，把机房编号赋值给
whatFeatureOfGroup：
public class UserThreadFactory implements ThreadFactory {
private final String namePrefix;
private final AtomicInteger nextId = new AtomicInteger(1);
// 定义线程组名称，在利用jstack 来排查问题时，非常有帮助
UserThreadFactory(String whatFeatureOfGroup) {
namePrefix = "FromUserThreadFactory's" + whatFeatureOfGroup + "-Worker-";
}
@Override
public Thread newThread(Runnable task) {
String name = namePrefix + nextId.getAndIncrement();
Thread thread = new Thread(null, task, name, 0, false);
System.out.println(thread.getName());
return thread;
}
}
3.【强制】线程资源必须通过线程池提供，不允许在应用中自行显式创建线程。
说明：线程池的好处是减少在创建和销毁线程上所消耗的时间以及系统资源的开销，解决资源不足的问题。如果不使用
线程池，有可能造成系统创建大量同类线程而导致消耗完内存或者“过度切换”的问题。
4.【强制】线程池不允许使用Executors 去创建，而是通过ThreadPoolExecutor 的方式，这样的处理方
式让写的同学更加明确线程池的运行规则，规避资源耗尽的风险。
说明：Executors 返回的线程池对象的弊端如下：
1）FixedThreadPool 和SingleThreadPool：
允许的请求队列长度为Integer.MAX_VALUE，可能会堆积大量的请求，从而导致OOM。
2）CachedThreadPool：
允许的创建线程数量为Integer.MAX_VALUE，可能会创建大量的线程，从而导致OOM。
3）ScheduledThreadPool：
允许的请求队列长度为Integer.MAX_VALUE，可能会堆积大量的请求，从而导致OOM。
5.【强制】SimpleDateFormat 是线程不安全的类，一般不要定义为static 变量，如果定义为static，必须
加锁，或者使用DateUtils 工具类。
正例：注意线程安全，使用DateUtils。亦推荐如下处理：
private static final ThreadLocal<DateFormat> dateStyle = new ThreadLocal<DateFormat>() {
@Override
protected DateFormat initialValue() {
return new SimpleDateFormat("yyyy-MM-dd");
}
};
说明：如果是JDK8 的应用，可以使用Instant 代替Date，LocalDateTime 代替Calendar，DateTimeFormatter 代替
SimpleDateFormat，官方给出的解释：simple beautiful strong immutable thread-safe。
6.【强制】必须回收自定义的ThreadLocal 变量记录的当前线程的值，尤其在线程池场景下，线程经常会
被复用，如果不清理自定义的ThreadLocal 变量，可能会影响后续业务逻辑和造成内存泄露等问题。
尽量在代码中使用try-finally 块进行回收。
正例：
objectThreadLocal.set(userInfo);
try {
// ...
} finally {
objectThreadLocal.remove();
}
7.【强制】高并发时，同步调用应该去考量锁的性能损耗。能用无锁数据结构，就不要用锁；能锁区块，就
不要锁整个方法体；能用对象锁，就不要用类锁。
说明：尽可能使加锁的代码块工作量尽可能的小，避免在锁代码块中调用RPC 方法。
8.【强制】对多个资源、数据库表、对象同时加锁时，需要保持一致的加锁顺序，否则可能会造成死锁。
说明：线程一需要对表A、B、C 依次全部加锁后才可以进行更新操作，那么线程二的加锁顺序也必须是A、B、C，否则可
能出现死锁。
9.【强制】在使用阻塞等待获取锁的方式中，必须在try 代码块之外，并且在加锁方法与try 代码块之间没
有任何可能抛出异常的方法调用，避免加锁成功后，在finally 中无法解锁。
说明一：在lock 方法与try 代码块之间的方法调用抛出异常，无法解锁，造成其它线程无法成功获取锁。
说明二：如果lock 方法在try 代码块之内，可能由于其它方法抛出异常，导致在finally 代码块中，unlock 对未加锁的对
象解锁，它会调用AQS 的tryRelease 方法（取决于具体实现类），抛出IllegalMonitorStateException 异常。
说明三：在Lock 对象的lock 方法实现中可能抛出unchecked 异常，产生的后果与说明二相同。
正例：
Lock lock = new XxxLock();
// ...
lock.lock();
try {
doSomething();
doOthers();
} finally {
lock.unlock();
}
反例：
Lock lock = new XxxLock();
// ...
try {
// 如果此处抛出异常，则直接执行finally 代码块
doSomething();
// 无论加锁是否成功，finally 代码块都会执行
lock.lock();
doOthers();
} finally {
lock.unlock();
}
10.【强制】在使用尝试机制来获取锁的方式中，进入业务代码块之前，必须先判断当前线程是否持有锁。
锁的释放规则与锁的阻塞等待方式相同。
说明：Lock 对象的unlock 方法在执行时，它会调用AQS 的tryRelease 方法（取决于具体实现类），如果当前线程不
持有锁，则抛出IllegalMonitorStateException 异常。
正例：
Lock lock = new XxxLock();
// ...
boolean isLocked = lock.tryLock();
if (isLocked) {
try {
doSomething();
doOthers();
} finally {
lock.unlock();
}
}
11.【强制】并发修改同一记录时，避免更新丢失，需要加锁。要么在应用层加锁，要么在缓存加锁，要么
在数据库层使用乐观锁，使用version 作为更新依据。
说明：如果每次访问冲突概率小于20%，推荐使用乐观锁，否则使用悲观锁。乐观锁的重试次数不得小于3 次。
12.【强制】多线程并行处理定时任务时，Timer 运行多个TimeTask 时，只要其中之一没有捕获抛出的异
常，其它任务便会自动终止运行，使用ScheduledExecutorService 则没有这个问题。
13.【推荐】资金相关的金融敏感信息，使用悲观锁策略。
说明：乐观锁在获得锁的同时已经完成了更新操作，校验逻辑容易出现漏洞，另外，乐观锁对冲突的解决策略有较复杂
的要求，处理不当容易造成系统压力或数据异常，所以资金相关的金融敏感信息不建议使用乐观锁更新。
正例：悲观锁遵循一锁二判三更新四释放的原则。
14.【推荐】使用CountDownLatch 进行异步转同步操作，每个线程退出前必须调用countDown 方法，线
程执行代码注意catch 异常，确保countDown 方法被执行到，避免主线程无法执行至await 方法，
直到超时才返回结果。
说明：注意，子线程抛出异常堆栈，不能在主线程try-catch 到。
15.【推荐】避免Random 实例被多线程使用，虽然共享该实例是线程安全的，但会因竞争同一seed 导致
的性能下降。
说明：Random 实例包括java.util.Random 的实例或者Math.random() 的方式。
正例：在JDK7 之后，可以直接使用API ThreadLocalRandom，而在JDK7 之前，需要编码保证每个线程持有一个
单独的Random 实例。
16.【推荐】通过双重检查锁（double-checked locking），实现延迟初始化需要将目标属性声明为
volatile 型，（比如修改helper 的属性声明为private volatile Helper helper = null;）。
正例：
public class LazyInitDemo {
private volatile Helper helper = null;
public Helper getHelper() {
if (helper == null) {
synchronized(this) {
if (helper == null) {
helper = new Helper();
}
}
}
return helper;
}
// other methods and fields...
}
17.【参考】volatile 解决多线程内存不可见问题对于一写多读，是可以解决变量同步问题，但是如果多
写，同样无法解决线程安全问题。
说明：如果是count++操作，使用如下类实现：
AtomicInteger count = new AtomicInteger();
count.addAndGet(1);
如果是JDK8，推荐使用LongAdder 对象，比AtomicLong 性能更好（减少乐观锁的重试次数）。
18.【参考】HashMap 在容量不够进行resize 时由于高并发可能出现死链，导致CPU 飙升，在开发过程
中注意规避此风险。
19.【参考】ThreadLocal 对象使用static 修饰，ThreadLocal 无法解决共享对象的更新问题。
说明：这个变量是针对一个线程内所有操作共享的，所以设置为静态变量，所有此类实例共享此静态变量，也就是说在
类第一次被使用时装载，只分配一块存储空间，所有此类的对象（只要是这个线程内定义的）都可以操控这个变量。
## (八) 控制语句
1.【强制】在一个switch 块内，每个case 要么通过continue / break / return 等来终止，要么注释说明
程序将继续执行到哪一个case 为止；在一个switch 块内，都必须包含一个default 语句并且放在最
后，即使它什么代码也没有。
说明：注意break 是退出switch 语句块，而return 是退出方法体。
2.【强制】当switch 括号内的变量类型为String 并且此变量为外部参数时，必须先进行null 判断。
反例：如下的代码输出是什么？
public class SwitchString {
public static void main(String[] args) {
method(null);
}
public static void method(String param) {
switch (param) {
// 肯定不是进入这里
case "sth":
System.out.println("it's sth");
break;
// 也不是进入这里
case "null":
System.out.println("it's null");
break;
// 也不是进入这里
default:
System.out.println("default");
}
}
}
3.【强制】在if / else / for / while / do 语句中必须使用大括号。
反例： if (condition) statements;
说明：即使只有一行代码，也要采用大括号的编码方式。
4.【强制】三目运算符condition ? 表达式1：表达式2 中，高度注意表达式1 和2 在类型对齐时，可能
抛出因自动拆箱导致的NPE 异常。
说明：以下两种场景会触发类型对齐的拆箱操作：
1）表达式1 或 表达式2 的值只要有一个是原始类型。
2）表达式1 或 表达式2 的值的类型不一致，会强制拆箱升级成表示范围更大的那个类型。
反例：
Integer a = 1;
Integer b = 2;
Integer c = null;
Boolean flag = false;
//  a*b 的结果是int 类型，那么c 会强制拆箱成int 类型，抛出NPE 异常
Integer result = (flag ? a * b : c);
5.【强制】在高并发场景中，避免使用“等于”判断作为中断或退出的条件。
说明：如果并发控制没有处理好，容易产生等值判断被“击穿”的情况，使用大于或小于的区间判断条件来代替。
反例：判断剩余奖品数量等于0 时，终止发放奖品，但因为并发处理错误导致奖品数量瞬间变成了负数，这样的话，
活动无法终止。
6.【推荐】当方法的代码总行数超过10 行时，return / throw 等中断逻辑的右大括号后需要加一个空行。
说明：这样做逻辑清晰，有利于代码阅读时重点关注。
7.【推荐】表达异常的分支时，少用if-else 方式，这种方式可以改写成：
if (condition) {
...
return obj;
}
// 接着写else 的业务逻辑代码;
说明：如果非使用if()...else if()...else...方式表达逻辑，避免后续代码维护困难，请勿超过3 层。
正例：超过3 层的if-else 的逻辑判断代码可以使用卫语句、策略模式、状态模式等来实现，其中卫语句示例如下：
public void findBoyfriend(Man man) {
if (man.isUgly()) {
System.out.println("本姑娘是外貌协会的资深会员");
return;
}
if (man.isPoor()) {
System.out.println("贫贱夫妻百事哀");
return;
}
if (man.isBadTemper()) {
System.out.println("银河有多远，你就给我滚多远");
return;
}
System.out.println("可以先交往一段时间看看");
}
8.【推荐】除常用方法（如getXxx / isXxx）等外不要在条件判断中执行其它复杂的语句，将复杂逻辑判
断的结果赋值给一个有意义的布尔变量名，以提高可读性。
说明：很多if 语句内的逻辑表达式相当复杂，与、或、取反混合运算，甚至各种方法纵深调用，理解成本非常高。如果赋
值一个非常好理解的布尔变量名字，则是件令人爽心悦目的事情。
正例：
// 伪代码如下
final boolean existed = (file.open(fileName, "w") != null) && (...) || (...);
if (existed) {
...
}
反例：
public final void acquire(long arg) {
if (!tryAcquire(arg) && acquireQueued(addWaiter(Node.EXCLUSIVE), arg)) {
selfInterrupt();
}
}
9.【推荐】不要在其它表达式（尤其是条件表达式）中，插入赋值语句。
说明：赋值点类似于人体的穴位，对于代码的理解至关重要，所以赋值语句需要清晰地单独成为一行。
反例：
public Lock getLock(boolean fair) {
// 算术表达式中出现赋值操作，容易忽略count 值已经被改变
threshold = (count = Integer.MAX_VALUE) - 1;
// 条件表达式中出现赋值操作，容易误认为是sync == fair
return (sync = fair) ? new FairSync() : new NonfairSync();
}
10.【推荐】循环体中的语句要考量性能，以下操作尽量移至循环体外处理，如定义对象、变量、获取数据
库连接，进行不必要的try-catch 操作（这个try-catch 是否可以移至循环体外）。
11.【推荐】避免采用取反逻辑运算符。
说明：取反逻辑不利于快速理解，并且取反逻辑写法一般都存在对应的正向逻辑写法。
正例：使用if(x < 628) 来表达x 小于628。
反例：使用if(!(x >= 628)) 来表达x 小于628。
12.【推荐】公开接口需要进行入参保护，尤其是批量操作的接口。
反例：某业务系统，提供一个用户批量查询的接口，API 文档上有说最多查多少个，但接口实现上没做任何保护，导致
调用方传了一个1000 的用户id 数组过来后，查询信息后，内存爆了。
13.【参考】下列情形，需要进行参数校验：
1）调用频次低的方法。
2）执行时间开销很大的方法。此情形中，参数校验时间几乎可以忽略不计，但如果因为参数错误导致中间执行回
退，或者错误，那得不偿失。
3）需要极高稳定性和可用性的方法。
4）对外提供的开放接口，不管是RPC / API / HTTP 接口。
5）敏感权限入口。
14.【参考】下列情形，不需要进行参数校验：
1）极有可能被循环调用的方法。但在方法说明里必须注明外部参数检查。
2）底层调用频度比较高的方法。毕竟是像纯净水过滤的最后一道，参数错误不太可能到底层才会暴露问题。一般DAO
层与Service 层都在同一个应用中，部署在同一台服务器中，所以DAO 的参数校验，可以省略。
3）被声明成private 只会被自己代码所调用的方法，如果能够确定调用方法的代码传入参数已经做过检查或者肯定不
会有问题，此时可以不校验参数。
## (九) 注释规约
1.【强制】类、类属性、类方法的注释必须使用Javadoc 规范，使用 /** 内容 */ 格式，不得使用 // xxx
方式。
说明：在IDE 编辑窗口中，Javadoc 方式会提示相关注释，生成Javadoc 可以正确输出相应注释；在IDE 中，工程调用
方法时，不进入方法即可悬浮提示方法、参数、返回值的意义，提高阅读效率。
2.【强制】所有的抽象方法（包括接口中的方法）必须要用Javadoc 注释、除了返回值、参数异常说明
外，还必须指出该方法做什么事情，实现什么功能。
说明：对子类的实现要求，或者调用注意事项，请一并说明。
3.【强制】所有的类都必须添加创建者和创建日期。
说明：在设置模板时，注意IDEA 的@author 为`${USER}`，而eclipse 的@author 为`${user}`，大小写有区别，而日期
的设置统一为yyyy/MM/dd 的格式。
正例：
/**
*
* @author yangguanbao
* @date 2021/11/26
*
**/
4.【强制】方法内部单行注释，在被注释语句上方另起一行，使用 // 注释。方法内部多行注释使用 /*  */
注释，注意与代码对齐。
5.【强制】所有的枚举类型字段必须要有注释，说明每个数据项的用途。
6.【推荐】与其用半吊子英文来注释，不如用中文注释说清楚。专有名词与关键字保持英文原文即可。
反例：“TCP 连接超时”解释成“传输控制协议连接超时”，理解反而费脑筋。
7.【推荐】代码修改的同时，注释也要进行相应的修改，尤其是参数、返回值、异常、核心逻辑等。
说明：代码与注释更新不同步，就像公路网与导航软件更新不同步一样，如果导航软件严重滞后，就失去了导航的意义。
8.【推荐】在类中删除未使用的任何字段和方法、内部类；在方法中删除未使用的参数声明与内部变量。
9.【参考】谨慎注释掉代码。在上方详细说明，而不是简单地注释掉。如果无用，则删除。
说明：代码被注释掉有两种可能性：1）后续会恢复此段代码逻辑。2）永久不用。前者如果没有备注信息，难以知晓注
释动机。后者建议直接删掉即可，假如需要查阅历史代码，登录代码仓库即可。
10.【参考】对于注释的要求：第一、能够准确反映设计思想和代码逻辑；第二、能够描述业务含义，使别
的程序员能够迅速了解到代码背后的信息。完全没有注释的大段代码对于阅读者形同天书，注释是给
自己看的，即使隔很长时间，也能清晰理解当时的思路；注释也是给继任者看的，使其能够快速接替
自己的工作。
11.【参考】好的命名、代码结构是自解释的，注释力求精简准确、表达到位。避免出现注释的另一个极
端：过多过滥的注释，代码的逻辑一旦修改，修改注释又是相当大的负担。
反例：
// put elephant into fridge
put(elephant, fridge);
方法名put，加上两个有意义的变量名称elephant 和fridge，已经说明了这是在干什么，语义清晰的代码不需要额外
的注释。
12.【参考】特殊注释标记，请注明标记人与标记时间。注意及时处理这些标记，通过标记扫描，经常清理
此类标记。线上故障有时候就是来源于这些标记处的代码。
1）待办事宜（TODO）：（标记人，标记时间，[预计处理时间]）表示需要实现，但目前还未实现的功能。这实际上是
一个Javadoc 的标签，目前的Javadoc 还没有实现，但已经被广泛使用。只能应用于类，接口和方法（因为它是一个
Javadoc 标签）。
2）错误，不能工作（FIXME）：（标记人，标记时间，[预计处理时间]）在注释中用FIXME 标记某代码是错误的，而
且不能工作，需要及时纠正的情况。
## (十) 前后端规约
1.【强制】前后端交互的API，需要明确协议、域名、路径、请求方法、请求内容、状态码、响应体。
说明：
1）协议：生产环境必须使用HTTPS。
2）路径：每一个API 需对应一个路径，表示API 具体的请求地址：
a）代表一种资源，只能为名词，推荐使用复数，不能为动词，请求方法已经表达动作意义。
b）URL 路径不能使用大写，单词如果需要分隔，统一使用下划线。
c）路径禁止携带表示请求内容类型的后缀，比如".json"，".xml"，通过accept 头表达即可。
3）请求方法：对具体操作的定义，常见的请求方法如下：
a）GET：从服务器取出资源。
b）POST：在服务器新建一个资源。
c）PUT：在服务器更新资源。
d）DELETE：从服务器删除资源。
4）请求内容：URL 带的参数必须无敏感信息或符合安全要求；body 里带参数时必须设置Content-Type。
5）响应体：响应体body 可放置多种数据类型，由Content-Type 头来确定。
2.【强制】前后端数据列表相关的接口返回，如果为空，则返回空数组[]或空集合{}。
说明：此条约定有利于数据层面上的协作更加高效，减少前端很多琐碎的null 判断。
3.【强制】服务端发生错误时，返回给前端的响应信息必须包含HTTP 状态码，errorCode、
errorMessage、用户提示信息四个部分。
说明：四个部分的涉众对象分别是浏览器、前端开发、错误排查人员、用户。其中输出给用户的提示信息要求：简短清
晰、提示友好，引导用户进行下一步操作或解释错误原因，提示信息可以包括错误原因、上下文环境、推荐操作等。
errorCode：参考
。errorMessage：简要描述后端出错原因，便于错误排查人员快速定位问题，注意不要包含敏
感数据信息。
正例：常见的HTTP 状态码如下
1）200 OK：表明该请求被成功地完成，所请求的资源发送到客户端。
2）401 Unauthorized：请求要求身份验证，常见对于需要登录而用户未登录的情况。
3）403 Forbidden：服务器拒绝请求，常见于机密信息或复制其它登录用户链接访问服务器的情况。
4）404 NotFound：服务器无法取得所请求的网页，请求资源不存在。
5）500 InternalServerError：服务器内部错误。
4.【强制】在前后端交互的JSON 格式数据中，所有的key 必须为小写字母开始的lowerCamelCase
风格，符合英文表达习惯，且表意完整。
正例：errorCode / errorMessage / assetStatus / menuList / orderList / configFlag
反例：ERRORCODE / ERROR_CODE / error_message / error-message / errormessage
5.【强制】errorMessage 是前后端错误追踪机制的体现，可以在前端输出到type="hidden" 文字类控
件中，或者用户端的日志中，帮助我们快速地定位出问题。
6.【强制】对于需要使用超大整数的场景，服务端一律使用String 字符串类型返回，禁止使用Long 类型。
说明：Java 服务端如果直接返回Long 整型数据给前端，Javascript 会自动转换为Number 类型（注：此类型为双精度浮
点数，表示原理与取值范围等同于Java 中的Double）。Long 类型能表示的最大值是263-1，在取值范围之内，超过253
（9007199254740992）的数值转化为Javascript 的Number 时，有些数值会产生精度损失。扩展说明，在Long 取值范
围内，任何2 的指数次的整数都是绝对不会存在精度损失的，所以说精度损失是一个概率问题。若浮点数尾数位与指数位
空间不限，则可以精确表示任何整数，但很不幸，双精度浮点数的尾数位只有52 位。
反例：通常在订单号或交易号大于等于16 位，大概率会出现前后端订单数据不一致的情况。
比如，后端传输的 "orderId"：362909601374617692，前端拿到的值却是：362909601374617660
7.【强制】HTTP 请求通过URL 传递参数时，不能超过2048 字节。
说明：不同浏览器对于URL 的最大长度限制略有不同，并且对超出最大长度的处理逻辑也有差异，2048 字节是取所
有浏览器的最小值。
反例：某业务将退货的商品id 列表放在URL 中作为参数传递，当一次退货商品数量过多时，URL 参数超长，传递到后端的
参数被截断，导致部分商品未能正确退货。
8.【强制】HTTP 请求通过body 传递内容时，必须控制长度，超出最大长度后，后端解析会出错。
说明：nginx 默认限制是1MB，tomcat 默认限制为2MB，当确实有业务需要传较大内容时，可以调大服务器端的限制。
9.【强制】在翻页场景中，用户输入参数的小于1，则前端返回第一页参数给后端；后端发现用户输入的
参数大于总页数，直接返回最后一页。
10.【强制】服务器内部重定向必须使用forward；外部重定向地址必须使用URL 统一代理模块生成，否
则会因线上采用HTTPS 协议而导致浏览器提示“不安全”，并且还会带来URL 维护不一致的问题。
11.【推荐】服务器返回信息必须被标记是否可以缓存，如果缓存，客户端可能会重用之前的请求结果。
说明：缓存有利于减少交互次数，减少交互的平均延迟。
正例：http1.1 中，s-maxage 告诉服务器进行缓存，时间单位为秒，用法如下，
response.setHeader("Cache-Control", "s-maxage=" + cacheSeconds);
12.【推荐】服务端返回的数据，使用JSON 格式而非XML。
说明：尽管HTTP 支持使用不同的输出格式，例如纯文本，JSON，CSV，XML，RSS 甚至HTML。如果我们使用的面
向用户的服务，应该选择JSON 作为通信中使用的标准数据交换格式，包括请求和响应。此外，application/JSON 是
一种通用的MIME 类型，具有实用、精简、易读的特点。
13.【推荐】前后端的时间格式统一为"yyyy-MM-dd HH:mm:ss"，统一为GMT。
14.【参考】在接口路径中不要加入版本号，版本控制在HTTP 头信息中体现，有利于向前兼容。
说明：当用户在低版本与高版本之间反复切换工作时，会导致迁移复杂度升高，存在数据错乱风险。
## (十一) 其他
1.【强制】在使用正则表达式时，利用好其预编译功能，可以有效加快正则匹配速度。
说明：不要在方法体内定义：Pattern pattern = Pattern.compile("规则");
2.【强制】避免用ApacheBeanutils 进行属性的copy。
说明：ApacheBeanUtils 性能较差，可以使用其他方案比如SpringBeanUtils，CglibBeanCopier，注意均是浅拷贝。
3.【强制】velocity 调用POJO 类的属性时，直接使用属性名取值即可，模板引擎会自动按规范调用POJO
的getXxx()，如果是boolean 基本数据类型变量（boolean 命名不需要加is 前缀），会自动调isXxx()
方法。
说明：注意如果是Boolean 包装类对象，优先调用getXxx() 的方法。
4.【强制】后台输送给页面的变量必须加 $!{var} ——中间的感叹号。
说明：如果var 等于null 或者不存在，那么 ${var} 会直接显示在页面上。
5.【强制】注意Math.random() 这个方法返回是double 类型，注意取值的范围0 ≤ x < 1（能够
取到零值，注意除零异常），如果想获取整数类型的随机数，不要将x 放大10 的若干倍然后取
整，直接使用Random 对象的nextInt 或者nextLong 方法。
6.【强制】枚举enum（括号内）的属性字段必须是私有且不可变。
7.【推荐】不要在视图模板中加入任何复杂的逻辑运算。
说明：根据MVC 理论，视图的职责是展示，不要抢模型和控制器的活。
8.【推荐】任何数据结构的构造或初始化，都应指定大小，避免数据结构无限增长吃光内存。
9.【推荐】及时清理不再使用的代码段或配置信息。
说明：对于垃圾代码或过时配置，坚决清理干净，避免程序过度臃肿，代码冗余。
正例：对于暂时被注释掉，后续可能恢复使用的代码片断，在注释代码上方，统一规定使用三个斜杠(///)
来说明注释掉代码的理由：
public static void hello() {
/// 业务方通知活动暂停
// Business business = new Business();
// business.active();
System.out.println("it's finished");
}
