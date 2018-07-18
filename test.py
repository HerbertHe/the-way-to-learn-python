#range()范围练习
for value in range(1,10):
    print(value)

#范围转数字列表练习
numbers=list(range(1,10))
print(numbers)

#奇数链表创建，加步长
odd_numbers=list(range(1,10,2))
print(odd_numbers);

#以下是数字列表及范围处理的几种写法
squares=[]
for value in range(1,10):
    square=value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,10):
    squares.append(value**2)
print(squares)

#这里的for语句没有冒号
squares=[value**2 for value in range(1,10)]
print(squares)

#数字统计计算练习(无输出)
digits=[1,2,3,4,5,5,6,7,8,0,9]
min(digits)
max(digits)
sum(digits)

#列表处理之切片(这玩意跟定范围差不多，不像之前的单个弹出去)
#省略写法的方式python通用(不写头从头始,不写尾到尾停,可以负数反着来)
players=['charles','martina','michael','florence','eli']
print(players[0:4])
print(players[:3])
print(players[4:])
print(players[-2:])#注意负数位置

#切片遍历
players=['charles','martina','michael','florence','eli']
for player in players[0:3]:
    print(player.title())

#复制列表和指向区别
my_players=['charles','martina','michael','florence','eli']
fri_players=my_players[:]
fri_players.append('liko')
print(my_players)
print(fri_players)

my_players=['charles','martina','michael','florence','eli']
fri_players=my_players#这玩意就是相当于指针的指向
fri_players.append('liko')
print(my_players)
print(fri_players)

#圆括号之元组(跟列表处理相似不过不能改单个元素)
dimensions=(200,15)
print(dimensions[0])
print(dimensions[1])
    #整体修改加遍历
dimensions=(200,29)
for dimension in dimensions:
    print(dimension)

#注意PEP8指南https://python.org/dev/peps/pep-00008/

#if语句演示
cars=['audi','bmw','subaru','toyota']

for car in cars:               #依然是注意冒号
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#检查条件即为逻辑运算(布朗值的运算)  一般有字符之转化成小写进行比较(在字符串无特殊要求的时候)
#相等、不等、大于、小于和与或非运算

#检查多个条件and or
age_0=22
age_1=1

print(age_0>2 and age_1<2)
print(age_0>2 or age_1<34)

#检查特定值在列表之中 in
cars=['audi','bmw','subaru','toyota']
print('audi' in cars)
print('sasa' in cars)

#检查特定值不在列表中 not in
cars=['audi','bmw','subaru','toyota']
if 'sasa' not in cars:
    print("sasa is not in cars")

#if语句之if-elif-else
#elif==else if
#多个elif做代码块，else可以省略，这些个玩意跟其他语言类似

#for循环变量调用列表的值可以跟if做嵌套
#确定列表是否为空,先调用if判断,举例:
#多个列表条件可以嵌套
requested=[]
#列表为空返回False
if requested:
    print("True")
else:
    print("False")

#注意由于程序的美观性和独立性，注意空格的使用

#------------------------------------------记得总结列表、元组、字典------------------------------------------------------
#字典结构
alien_0 = {'color' : 'green','point': 5 }
print(alien_0['color'])
print(alien_0['point'])

#其中的'color'一类称为键,而'green'一类称为其值
#召唤键，返回值                key & value

#添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  #这玩意的打印跟列表一样，python只关心键-值匹配的关系

#键的值修改
alien_0['color'] = 'yellow'
print(alien_0['color'])

#删除键-值对，永远消失
del alien_0['point']
print(alien_0)

#字典这玩意可以用来撞库和检索，创建个空的在后面加key和value
#字典这玩意可以多行搞，再加个字符串拼接啥的美滋滋

#遍历所有键-值对.items()
#---即用俩变量，for循环。。。for key,value in zidian.items():
alien_0 = {'color' : 'green','point': '5' }          #注意不能打印int，必须转化成str
for key,value in alien_0.items():
    print(key.upper()+value)

#遍历所有的键.keys()
# //.keys()可以省略，python默认遍历键
# //顺序输出有sorted(zidian.keys())
#---用一个变量，for循环。。。for key in zidian.keys():
for key in alien_0.keys():
    print(key.upper())

#遍历所有的值.values()
# //重复有set()
# //集合关系有set(zidian.values())
#---用一个变量，for循环。。。for value in zidian.values():
for value in alien_0.values():
    print(value.title())

#字典可以跟列表互相嵌套，也可以自身嵌套
#举个例子
#储存外星人的空列表
aliens = []

#代码创建外星人
for alien_num in range(30):
    alien = {'color' : 'green' ,'point' : 5}
    aliens.append(alien)
print(aliens)
print("创建外星人的数目为:"+str(len(aliens)))

#修改特定特征的外星人
for alien in aliens:
    if alien['color'] == 'green':
        alien['point'] = 10 ;
print(aliens)

#字典中嵌套列表

fav_languages={
    'jen':['python','ruby'],
    'sara':['c'],
    'edward':['java','go'],
    'phil':['python','haskell'],
    }
for name,languages in fav_languages.items():                             #注意缩进别乱打空格
     print("\n"+name+"'s fav languages following")
     for language in languages:
         print("\t"+language)


#输入函数input()#字典嵌套字典
#---就是键->键->值这样多重嵌套的结果

# //在python2.x输入是raw_input

#message=input("提醒用户输入部分：")
#print(message)

#多行字符串提示方法,变量储存字符,然后字符串运算，然后再输出，记得加\n
#prompt="这是第一行"
#prompt+="\n这是第二行"
#string=input(prompt)
#print(string)

#input是字符串输入，可以用int()进行类型转换得到整型的数
#求模运算也就是取余运算%
#evennumber偶数,oddnumber奇数

#while当型循环，注意实际情况的对于条件的需要情况，，当然可以设置标志变量控制条件False or True
#强制退出break，跳出循环continue

number=0
while number<=10:
    number+=1
    if number%2==0:
        continue
    print(number)

#注意死循环的运用情况
confirmed=[]
unconfirmed=['a','b','c']
#注意写法
while unconfirmed:
    confirmed.append(unconfirmed.pop())                    #精简写法
    for user in confirmed:
        print(user)

#while用来删除列表的特定值.remove()
pets=['dog','cat','rabbit','goldfish','cat','dog']

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#while用来字典输入
#设置控制循环的标志变量
#注意字典的写入！！！！！！----------------------ctrl + /  整段注释和消除   或者""" """-----------------------------------
# responses={}
# active=True
# while active:
#     name=input("please input the name")
#     response=input("please input the response")
#     responses[name]=response
#
#     repeat=input("if other needs to be asked?(y/n)")
#     if repeat == 'n':
#         active =False
#
# print("the results are followed")
# for name,response in responses.items():
#     print(name +"\t"+ response)

#字典写入的两个变量的键-值对关系的配对

#定义函数之def 在C中是函数类型的定义比如int void float double啥的
#之前就定义了需要传递的参数变量
def greet_user(username):
    print("Hi "+username)
greet_user('joole')

# def 这是一个函数(hanshu):
#     print(hanshu)
# 这是一个函数('222')

#实参顺序关联称为位置实参
#名称-值对应的关键字实参,无关位置，直接赋值
def des_pet(animal_type,pet_name):
    print("动物种类"+animal_type)
    print("宠物名称"+pet_name)
des_pet(animal_type='dog',pet_name='jojo')
#可以直接在函数中预设默认值，这一点跟C不一样

#预设默认值为空可以使那一项的形参变为可选的！！！！！！！！！！！！！！！！！！！！！！！！！！！

#函数可以混用位置实参，关键字实参和默认值
#建议可以的情况下尽量与C统一避免C编程的不必要的麻烦
#返回值return返回给函数，返回值可以是字符串、列表、字典，，-------------------------任意类型--------------------------------

#可以向函数传递列表，一改都改了

#function_name(list_name[:])通过切片做副本

#传递任意数目的实参。。。          *了解一下，这玩意也就是个---------元组---------。。。
#使用任意数目的关键字实参。。。      **了解一下，这玩意也就是个------字典---------。。。键值对的匹配！！！-------------------
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('ddsdsds','sadasdas','asddasdaasd','asdasdsadasd')

"""
结合使用位置实参和任意数量实参的时候！！！一定要把任意数目的实参放在最后guess why？
"""

"""
import 用于导入模块
要在同一目录下.py文件，，然后.运算了解一下
"""


