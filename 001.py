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

字符串运算：  +  字符串连接 
             *  重复字符串
             [] 访问字符串的某一个字符(从0开始) 
              









































 







