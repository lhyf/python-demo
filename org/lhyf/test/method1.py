numStr = input("请输入一个整数")
num = int(numStr)
if num > 100 or num < 0:
    print("输入错误")
elif num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("E")