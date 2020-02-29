try:
    10 / 0
except ZeroDivisionError:
    print("程序出错了")
else:
    print("程序正常运行的")
finally:
    print("程序执行完了")


def add(arg1, arg2):
    if arg1 < 0 or arg2 < 0:
        raise Exception("参数不能有负数")

    return arg1 + arg2


add(1, 2)
print(None)