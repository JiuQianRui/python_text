
'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类,pass代表直接跳过
    # 此处pass必须有
    pass

#　定义一个对象
mingyue = Student()

#　在定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    coure = "python"

    # 需要注意
    #　１,def dohomework的缩进层次
    #　２,系统默认出一个swlf参数
    def dohomework(self):
        print("我在做作业")

        # 推荐咋函数末尾使用return
        return None

# 实例化一个叫yueyue的学生,是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue .age)
# 注意成员函数的调用 没有传入参数
yueyue.dohomework()