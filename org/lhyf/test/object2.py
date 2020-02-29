class Animal:
    "动物类"

    def __init__(self, name):
        self._name = name

    def run(self):
        print("动物会跑")

    def sleep(self):
        print("动物会睡觉")


class Dog(Animal):
    def __init__(self, name, age):
        # super() 可以用来获取当前类的父类
        super().__init__(name)
        # self._name = name
        self._age = age

    def bark(self):
        print("狗会叫")


dog = Dog("小黑",12)
dog.run()
dog.bark()
