class Student:
    """一个Student类"""
    address = ""
    def __init__(self, name, age):
        # __name --> _Student__name
        self.__name = name
        self.__age = age

    def info(self):
        print("My name is{}, im {} years old".format(self.__name, self.__age))
        print("My address is {}".format(self.address))


s1 = Student("小青", 18)
s1.address = "辽宁"
s1.info()


class Person:

    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 装饰器 用来将一个get方法转换为对象的属性
    # 添加
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age



p = Person("小青")
print(p.name)