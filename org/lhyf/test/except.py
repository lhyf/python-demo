def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print("参数没有包含数字\n")

def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

def excp():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            break
        except ValueError as err:
            print("您输入的不是数字，请再次尝试输入!",err)


def test():
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

