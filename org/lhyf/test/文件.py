file_name = "demo.txt"

# 自动关闭打开的文件 with as
try:
    with open(file_name, encoding="utf-8") as file_obj:
        print(file_obj.read())
except FileNotFoundError as e:
    print("{} 文件未找到".format(file_name))

print("*" * 30)

try:
    with open(file_name, encoding="utf-8") as file_obj:
        chunk = 10

        while True:
            content = file_obj.read(chunk)
            print(content, end="")
            if not content:
                break
except FileNotFoundError as e:
    print("{} 文件未找到,异常消息为:{}".format(file_name, e))

print("-" * 30)

try:
    with open(file_name, encoding="utf-8") as file_obj:
        for line in file_obj:
            print(line, end="")
except:
    print("文件读取出错了")
