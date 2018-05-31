'''
定义一个学生类
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 在定义一个类，描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    #需要注意
    # def doHomework的所经登记
    # 系统默认有一个self参数
    def doHomework(self):
        print('I 做作业')

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()