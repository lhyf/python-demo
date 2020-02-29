def sayHello(name, age=12):
    print("我叫:", name, ", 今年", age, "岁了.")


sayHello(name="小青")

print(str(None))


def printinfo(arg1, *vartuple):
    "加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。"
    print("输出:")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(10, 11, 12)


def printInfo2(arg1, **var):
    "加了两个星号 ** 的参数会以字典的形式导入。"
    print("输出:")
    print(arg1)
    for (k, v) in var.items():
        print(k, v)
    return


# 辽宁 与 河南 不能使用引号
printInfo2("开始", 辽宁 = "沈阳",河南="郑州")

# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

"""
必须参数
关键字参数
默认参数
不定长参数: * 以元组形式传入, ** 以字典形式传入

"""