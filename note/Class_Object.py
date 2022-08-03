# 面向对象


class Student(object):
    # 类属性
    person = 'student'

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('构造函数执行')

    def __del__(self):
        print('析构函数执行') # 这个方法 python 会自己调用对对象进行垃圾回收

    # 类方法
    @classmethod
    def classMeth(cls, param):  # 第一个参数是本类，第二个参数时调用方方法传入的参数
        print('这是一个类方法:{}，引用类属性:{}，参数:{}'.format(cls, cls.person, param))

    # 实例方法
    def show(self):
        print('My name is {},I am {} years old'.format(self.name, self.age))

Student.classMeth('noby')
# 为类新添加一个类属性
Student.star = 'earth'
print(Student.star)


# 对象的实例化
print('\n-------------')
noby = Student('noby',21)
print(noby.show())
del noby # 销毁一个对象

# type(obj)：来获取对象的相应类型；
# isinstance(obj, type)：判断对象是否为指定的 type 类型的实例；
# hasattr(obj, attr)：判断对象是否具有指定属性/方法；
# getattr(obj, attr[, default]) 获取属性/方法的值, 要是没有对应的属性则返回 default 值（前提是设置了 default），否则会抛出 AttributeError 异常；
# setattr(obj, attr, value)：设定该属性/方法的值，类似于 obj.attr=value；
# dir(obj)：可以获取相应对象的所有属性和方法名的列表：


