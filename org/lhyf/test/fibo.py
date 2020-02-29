def fib(index):
    "返回斐波拉契数列的值"
    if index == 1:
        return 1
    elif index == 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def create_fib(n):
    "创建一个含有n项的斐波拉契数列"
    print(__name__)
    list = []
    while n >= 1:
        list.insert(0, fib(n))
        n -= 1
    return list


if __name__ == "__main__":
    fibo = create_fib(1)
    print(fibo)
