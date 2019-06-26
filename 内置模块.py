import math # 导入数学模块
# print(math) (引用数学模块)
'''
celi() 向上取整操作
print(math.ceil(9.7)) 打印出来是10
print(math.ceil(5.1)) 打印出来是6


fioor() 向下取整操作
print(math.floor(5.01)) 打印出来是5
print(math.floor(3.4)) 打印出出来是3


查看系统保存的关键字,不可以用来当做变量的命名
import keyword
pringdkeyword.kwlist)

# round() 四舍五入操作 python内置函数
print(round(5.01)) # 结果是5
print(round(5.5))  # . . .6
print(round(5.9)) # . . . 6


# sprt() 开平方,返回的是浮点数
print(math.sqrt(4)) #. . .2.0

# pow() 与幂运算差不多,计算一个数的几次方,返回浮点型
print(math.pow(4,3)) # 第一个参数是底数,第二个是指数,结果是64.0
# 幂运算 返回整形
print(4**3)  # . . .64


# fabs() 对一个数值获取它的绝对值,返回浮点数
print(math.fabs(-1))
print(math.fabs(3))
# abs() 获取绝对值操作 不是数学模块中的,是python内置函数,返回值是本身的类型
print(abs(-1))

# fsum() 对整个序列求和,返回浮点数
print(math.fsum[1,2,3,4,5])
# sum() python内置求和,返回值由本身类型而定
print(sum[1,2,3,4,5])

# math.modf() 将一个浮点数分为整数部分和小数部分组成元组  (结果是小数部分在前,整数在后)
print(math.modf(4.5))  # 结果是(0.5,4.0) 返回的值是浮点数
print(math.modf(0))    # . . .(0.0,0.0)
print(math.modf(3))    # . . .(0.0,3.0)

# copysign() 将第二个数的符号(正负号)传给第一个数  返回的是第一个数的浮点数
print(math.copysign(2,-3))  # . . .-2.0
print(math.copysign(-7,4)) # . . .7.0

# 打印自然对谁e 和π的值
print(math.e) 
print(math.pi) 
'''

import random
# random()获取0-1之间的随机小数 包含0,不包含1
#for i in range(10):
    # print(random.random())
    # 打印10次0-1之间的随机小数

    # random.randrange() 获取指定和开始之前的整数值,可以指定间隔值
    # print(random.randrange(1,9))

    # uniform() 随机获取指定范围内的值(包括小数)
    # print(random.uniform(1,9))

'''
# choice() 随机获取列表中的一个值
print(random.choice([1,4,5,6,7,3,3]))

# shuffle() 随机打乱序列 返回值是空
liat1 = [1,23,3,45,5,63,7]
print(liat1)
random.shuffle(liat1)
print(liat1)
'''
