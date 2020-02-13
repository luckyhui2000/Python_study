&&&&&程序执行的过程：自上而下顺序执行（面向过程）





#print函数
print("hello", "world")



# input函数
age = input("请输入你的年龄: ")  *****“等待输入“



#Python数据类型
计算机能处理的远远不止数值，还可以处理文本，图形，音频，视频网页等
Number  数字: 整数 浮点数 复数
String 字符串          *****(没有字符的概念但也存在,"s")
Boolean布尔值
None     空值
list     列表
tuple    元组
dict     字典
set      集合



#标识符
含义：是一串字符串          *****字符串未必是标识符
规则: 只能由字母 数字 下划线组成
      开头不能为数字
      不能是Python的关键字  *****保留字(保留以后当作关键字); import keyword
                            *****                          print(keyword.kwlist)
      区分大小写
      见名知意
      遵循驼峰原则          *****首单词是正常的，从第二个单词开始首字母大写；sunckGoodMan
作用：给 变量 函数等命名
注意：在python中，非ASCII标识符也是允许的



#变量和常量
变量：概述1：      程序可操作的存储空间的名称     @@@@@ 0x100 0x代表16进制数  常用于计算机内存地址
      概述2：      程序运行期间能改变的数据
      概述3：      每个变量都有特定的类型
      作用：       将不同类型的数据存储到内存
      定义变量：    变量名 = 初始值             *****初始值：为了确定变量的类型
      数据的存储：  变量名 = 数据值             !!!!!在使用前必须定义，否则会报错
      辨别：       num1 = input()      num2 = input()       print(num1 + num2)
                   num1 = int(input()) num2 = int(input())  print(num1 + num2)
      删除变量：    del 变量名
      查看类型：    type(变量名)
      查看地址：    id(变量名)                 *****变量的首地址

常量：程序运行期间不能改变的 

&&&&&连续定义多个变量
      num1 = num2 = 
&&&&&交互式赋值定义变量
      num1， num2 = 数值1， 数值2 


#数字类型
整数                                          *****Python可以处理任意大小的整数；
浮点数：      由整数部分和小数部分组成，浮点数运算可能会有四舍五入的误差
复数：        由实数部分和虚数部分组成

数字类型转换： int("123")=123 int(1.9)=2
              float(1)=1.0                    !!!!!字符串中出现其他无用字符会报错



#数学功能     import math                     *****引入math库 
abs()             返回数字的绝对值
max(, , ,)        返回给定参数的最大值
min(, , ,)        返回给定参数的最小值
pow(x,y)          返回x的y次方
round(x，[y])     返回四舍五入后的值           *****保留n位小数,无n默认取整

import math
math.ceil()       返回向上取整后的值
math.floor()      返回向下取整后的值
math.modf()       返回整数部分和小数部分
math.sqrt()       返回平方后的数值

import random
random.choice([, , , ,])     随机从序列的元素中返回一个值       *****该序列中的元素可以为字符串
random.choice(range(5))      ==random.choice([0,1,2,3,4])      *****random.choice(range(100) + 1) 
random.choice("sunck")       ==random.choice("s""u""n""k")
random.randrange(1, 100, 2,) 随即选其1到100之间的奇数
random.randrage([start,] stop [, step])                        *****格式；默认值：start=0,step=1
random.random()              随机生成[0,1)之间的随机数
random.shuffle(list)         将列表list中的元素随机排列
random.uniform(a, b)         随机生成一个[a,b]中的实数
   


#运算符与表达式
表达式:      定义:由变量 常量和运算符组成的式子
            阅读: <<功能和值

算术运算符： + - * / % ** //

复合运算符： += -= ......

位运算符：   *****把数字看作二进制数来运算
            &（按位与运算符）         
            |（按位或运算符）
            ^（按位异或运算符）   *****二进制两位相异时，结果为1。
            ~（按位取反运算符）   *****每个二进制数据位取反。
            <<（左移运算符）      *****各二进制位全部左移若干位，由<<右侧的数字决定，高位丢弃，低位补0。
            >>（右移运算符）      *****由>>右侧数字决定
            
关系运算符： ==   !=   >   <   >=   <=   
值：如果成立则整个关系运算式的值为真；否则为假。

逻辑运算符：  and（逻辑与）        值：见假则假      @@@@@短路原则：表达式1 and 表达式2 and 表达式3   表达式1为假则后面不会运算
              or（逻辑或）        值：见真则真
             not（逻辑非）        值：真假颠倒
     
成员运算符：  in：如果在指定的序列中找到值则返回True，否则返回False
             not in：与in相反
             
身份运算符：  is：   判断两个标识符是不是引用同一个对象
	     is not：判断两个标识符是不是引用不同的对象
	     
!!!!!运算符的优先级：  **
                      ~ + -   正负号（一元加减）
                      * / % //
                      + -
                      >> <<
                      &
                      ^ |
                      <= < > >=
                      == !=
                      = %= += -= //=   赋值运算符
                      is   is not
                      in   not in
                      and or not
                      
                          
                          
#if语句
格式：
if 表达式:
	语句

逻辑：首先计算表达式的值，如果该值为真，则执行语句。否则跳过。

*****何为真假？
*****假：0 0.0 " None False
*****非假即真


#if-else语句
格式：
if 表达式:
	语句1
else:
	语句2

逻辑:首先计算表达式的值，为真则执行语句1，跳出if-else语句；执行语句2跳出if-else语句。



#String字符串：以单引号或双引号括起来的任意文本。
创建字符串：str1 = "I am a good man"    !!!!!字符串不可变*****

字符串运算：     +  字符串连接 
                *  重复字符串
                [n] 访问字符串的某一个字符(从0开始) 
                [a,b]  截取字符串        ****a b可以为空
                in    not in      
                
字符串比较大小：
规则：从第一个字符开始比较，谁的ASCII值大谁就大，如果相等就比较下一个字符的大小，不一定长度是短的以|0（码为0）替补           
                


#格式化输出
num = 10   str1 = "HelloWorld"  f1 = 1.23
print("num = %d, str1 = %s, f1 = [.n]f" % (num, str1, f1))     *****精确到小数点后n位
*****占位符：%d 整数占位  %s 字符串占位  %f 浮点数占位



#转义字符(\):  将一些字符转换成有特殊含义的字符               *****占一个字符
\\n                                                         *****将\n输出
输出引号：     \"
               "Hello 'World'"   'Hello"world"'

换行符：       \n
               print('''
               1
               2
               ''')

制表符：       \t

*****如果字符串中有好多转义，为了简化，python允许用r表示内部的字符串默认不转义



#字符串中的功能
eval(str1)
功能：将字符串str1当成有效的表达式求值并返回计算结果
例: print(eval(12 + 12))  >>>  24

len(str1)
功能：返回字符串的长度（字符个数）

str1.lower()
功能：新生成的字符串中转换字符串中大写字母为小写

str1.upper
功能：为大写

str1.swapcase()
功能：新生成的字符串中大小写互换

str1.capitalize()
功能：首字母大，其他小写

str1.title()
功能：每个单词的首字母大写

str1.center(width[, fillchar])       *****char：字符(character)
功能：返回一个指定宽度的字符串str1剧中使用fillchar填充默认空格
print("hello".center(10, "*")) >>> **hello***

str1.ljsut(width[, fillchar])
功能：返回一个指定宽度的左对齐字符串使用fillchar填充默认空格

str1.rjust(width[, fillchar])
功能：返回一个指定宽度的右对齐字符串使用fillchar填充默认空格

str1.zfill(width)
功能：返回一个长度为width的字符串，右对齐，前面补0(zero)

str1.count("xxx"[, start][, end])
功能：返回字符串中xxx出现的个数，可以制定一个范围，默认从头到尾

str1.find("xxx"[, start][, end])
功能：返回xxx第一次出现的开始下标，从左至右检测；没有返回-1

str1.rfind("xxx"[,start, end])
功能：从有向左查找

str1.index("xxx"[start, end])
功能：和find一样，只不过当xxx不存在是会报一异常

str1.rindex()

str1.lstrip(["xxx"])
功能：返回截掉左侧的字符后的字符串(默认为空格)

str1.rlstrip(["xxx"])

str1.strip
功能：从两侧截取

str1.split("xxx"[, n})   ***** 默认全截取
功能:以xxx为分隔符截取字符串,指定n则默认n个字符串,剩下的放在一起不截取,返回列表
print("*i*am*a*good*man*".split("*"))
>>>['', 'i', 'am', 'a', 'good', 'man', '']

str1.splitlines([keepends])   keepends == True 会保留换行符默认为 False
功能：安装('\r','\r\n','\n')分隔,返回一个列表

"x".join(列表名)
功能：列表中元素组成字符串用x分隔

max() min()
功能:返回最大最小的字符以AScii码表比较

str1.replace("被替换","替换",[n])   *****默认全部替换,从前开始替换
功能：返回替换后的一个字符串  *****字符串不可变

str1.maketrans()
功能：返回一个字符串的映射表

str1.strip
功能：从两侧截取

str1.startwith(字符串[, start][, end])
功能：判断在指定的范围内是否以某一字符串开头

str1.endwith(字符串[, start][, end])
功能：判断在指定的范围内是否以某一字符串结尾

str1.encode("utf-8", "ignore")  *****ignore:错误不处理
功能：进行编码

str1.decode()
功能：进行解码
!!!!!要与编码是的格式一致

str1.isalpha()
功能：字符串中至少有一个字符且所有的字符都是字母时返回true,否则返回false

str1.isalnum()
功能：字符串中至少有一个字符且所有的字符都是（字母或数字）时返回true,否则返回false

str1.isupper()
功能：字符串中至少有一个英文字符且所有的英文字符都是大写时返回true,否则返回fals

str1.islower()

str1.istitle()
功能：如果字符串是标题化的则返回True,否则返回False

str1.isdigit()
功能：字符串中至少有一个数字字符且只包含数字字符时返回True，否则返回False

str1.isnumeric()
功能：同上

str1.isdecimal()
功能：字符串至少包含一个字符只包含十进制字符时返回True，否则返回False

str1.isspace()
功能：字符串中至少有一个空格且只包含空格时返回True，否则返回False
*****"/n" "/r" "/t" 时返回True



#while循环语句
格式：
while 表达式:
	语句
逻辑：当程序执行到while时，先计算表达式的值，如果表达式的值为假，那么结束整个while语句，
      如果表达式的值为真，执行语句，再计算表达式的值.....
      
!!!!!层级的嵌套最好不能超过三层    
      
      
      
#布尔值与空值
布尔值：只有True和False两种

空值：是python里一个特殊的值，None在python中不能当作0来处理。因为0是有意义的，而None是一个特殊值。



#list列表
本质：一种有序的集合
功能：存储多个数值
格式：
列表名 = [列表选项1, .., .., .., ..]
[]                   *****空列表
!!!!!列表中元素可以是不同类型的数据类型

列表名[下标]         *****取值
列表名[下标] = 数据  *****替换
!!!!!元素的访问不能越界即下标不能超出范围

列表操作：         *****参考字符串
	列表组合： 新列表 =  列表1 + 列表2
	列表重复： 列表 * n
	判断元素是否在列表中： in   ****成员运算符
	列表截取： 列表[a: b]

二维列表：[[], [], [] ]

列表方法：
	追加元素: list1.append(元素)    *****在列表的末尾
	追加另一个列表中的多个元素：list1.estend([])
	在列表中插入一个元素：list1.insert(下标,元素)
	删除元素并返回该元素：list1.pop(n) *****n为下标默认为最后一个元素下标
        删除指定元素： list1.rm(元素)    *****仅删除第一个
        清除列表中的所有元素：list1.clear()
        从列表中寻找某个元素并返回该元素的下标：list1.index(元素,[start],[stop])   *****第一个
        列表中元素个数： len(list1)
        返回列表中最值：max(list1)   min(list1)
        某元素在列表中重复的次数：list1.count(元素)
        元素倒序：list1.reverse()
        元素排序：list1.sort()     *****升序
        深拷贝：list2 = list1.copy()                 *****内存拷贝
        浅拷贝：list1 = [1, 2, 3,]                   *****引用拷贝
                list2 = list1
                list2[0] = 100
                print(list1, list2)
                print(id(list2), id(list2))
                >>> 
        
	@@@@@内存：
		  栈区：系统自动分配，程序结束释放内存空间   ****普通变量存储位置
		  堆区：程序员手动开辟，手动释放  ****对象存储位置 
	          list1 = [1, 2, 3] *****list1存储在栈区(1，2，3的二进制位置)     1 2 3 存储在堆区
        
        将元组转化列表：list1 = list((1,2,3,4))
 	
 
 
#条件控制语句
if-elif-else 语句：
	格式：
	if 表达式1:
		语句1
	elif 表达式2:
		语句2
	elif 表达式3:
		语句3
	else：       *****可有可无
		语句e
 
	逻辑：首先计算表达式1的值：如果为真则执行语句1，之后跳过整个 if-elif-else 语句
	      如果为假则计算表达式2的值，为假则跳过整个 if-elif-else 语句，为真执行语句2
	      如果所有表达式为假且有else则执行语句e
	      每个el都是上面表达式的否定

死循环：表达式永远为真的循环

while - else 语句：
	格式：
	while 表达式：
		语句1
	else:
		语句2

逻辑：在条件语句（表达式）为false时执行else中的“语句2” 。
       

for 语句：
	格式：
	for 变量名 in 集合:
		语句
	
	逻辑：按顺序取集合中的每个元素赋值给变量，再去执行语句，如此循环，直到取完集合中的元素为止

#range([start,] end[, step])函数：     *****列表生成器   默认start=0 stet=1
格式：
range(n)
功能：生成[0,n-1]的一个数列
for x in range(10)     *****执行十次

for index, n in enumerate([1, 2, 3, 4, 5])
	print(index, n)    *****同时返回下标和元素



#break语句：
作用：结束 for 和 while 循环
!!!!!:只能跳出距离他最近的那一层循环，不会执行 else 下面的语句



#continue语句：
作用：跳过当前循环中的剩余语句，然后继续下一次循环



#turtle模块绘图         *****简单的绘图工具
理解：为一个机器人，只能听懂有限的命令
用法： import turtle
命令：
	运动命令：turtle.forward()   向前移动长度
		 turtle.backward()   向后移动长度
		 turtle.right()    向右转移度数
		 turtle.left()
		 turtle.goto(x,y)   移动到坐标为（x,y）的点
		 turtle.speed()     移动速度(0~10)
!!!!! 默认原点在(0,0)

	笔画控制命令：turtle.up() 笔画抬起
	             turtle.down() 笔画落下
	             turtle.setheading()   改变海龟的朝向
	             turtle.pensize()    宽度
	             turtle.pencolor("Red")   颜色
	             turtle.reset()   恢复所有设置，清空窗口，重置turtle状态
	             turtle.clear()   清空但不会重置设置
	             turtle.circle(r,steps=n)  绘制一个圆形   n>1时为n边形
	             turtle.begin_fill()
	             turtle.fillcolor(colorstr)   颜色填充
	             turtle.end_fill()
	             
	             
	其他命令 ：turtle.done()  程序继续执行
                  turtle.undo()  撤销上一次指令
                  turtle.hideturtle()    海龟隐藏
                  turtle.showturtle()    海龟显示
                  turtle.screensize(,)   画板大小
                  
                  
                  
#元组
创建元组:
tuple1 = (,,,,,)  *****只有一个元素时后面也要加逗号

元组元素的访问:
格式:
元组名[下标]               *****下标从0开始   下标为 -1 时为到数第一个

元组的修改:          *****元组中的元素不可变 ,元组中列表元素中的元素可变
                    @@@@元组中储存列表元素的地址,列表可变
                    
元组的删除:       del 元组名

元组的操作:	
	加法 乘法
	in   判断是否在元组中
	元组名[开始下标:结束下标 ]   元组的截取(开始下标开始到结束下标之前)
	
二维元组:((),(),())

元组的方法:
	len()
	max()  min()
	tuple(list1)     列表转元组

意义:不可变,更安全



#字典
概述：使用键-值（key-value）存储，具有极快的查找速度 *****value：数据
!!!!!字典是无序的

keyd的特性：
1.一个字典中含有多个键-值对，但key必须唯一
2.key必须是不可变的对象
3.字符串、整数等都是不可变的，可以作为key
4.list是可变的，不能作为key

思考：保存多位学生的姓名和成绩
使用字典，学生姓名为key，成绩为值
dict1 = {"tom":60, "lilei":70}

元素的访问：

dict1[key]
功能：获取值
*****没有key的时候会报错

dict1.get(key)
功能：获取值，但没有时会返回 None

dict1[key] = 值
功能：添加
*****新添key重复原有key时覆盖即修改

dict1.pop(key)
功能：删除key

字典的遍历：           *****遍历: 按一定规则访问一个非线性的结构中的每一项, 强调非线性结构(树, 图).
                                  而迭代一般适用于线性结构(数组, 队列).

for key in dict1:
	print(key, dict1[key])

for value in dict1.value():
	print(value)

for k, v in dict1.items():
	print(k, y)

for i, V in enumerate(dict1):
	print(i, V)


与list比较：
	1.查找和插入的速度极快，不会随着key-value的增加而变慢
	2.需要占用大量的内存
	3.list随着数据量的增多查找和插入的速度变慢
	4.list占用空间相对较小

例题：使用字典统计一字符串中的重复单词的次数
     1.以空格切割字符串，生成列表
     2.循环处理列表中的每个元素
     3.以元素key提取空字典
     4.如果没有提取到返回 None ，就以该元素为key，1为value存进字典
     5.如果提取到，将对应key的value修改并加一



#set
概念：类似dict，是一组key的集合，不存储value，是无序无重复元素的集合

创建：需要一个list、tuple或者dict作为输入集合
s1 = set([1, 2, 3, 4, 4])
print(s1)
>>>{1, 2, 3, 4}
*****重复元素在会被自动过滤

添加：
s1.add()
*****可以添加重复的但会自动滤过














 
 
 
 
 
 
 


