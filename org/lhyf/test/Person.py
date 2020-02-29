class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__() 这个方法将会在尝试将这个对象转换为字符串的时候调用
    # 它的作用可以用来将对象转换为字符串
    def __str__(self):
        # return "Person[name:{},age:{}]".format(self.name, self.age)
        return "Person[name:%s,age:%d]" % (self.name, self.age)

    # 当对当前对象使用repr 函数时调用
    # 它的作用是指定对象在 "交互模式" 中直接输出的效果
    def __repr__(self):
        return "repr"

p1 = Person("小青", 18)
p2 = Person("小红", 20)

print(p1)
print(str(p1))
print(repr(p1))