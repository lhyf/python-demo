import random

target = random.randint(1,10)
print("猜猜我想的数字")
temp = input("请输入一个数字:")
num = int(temp)
while True:
    if num == target:
        print("哇,你猜对了")
        break
    else:
        if num > target:
            print("太大了")
        else:
            print("太小了")
        temp = input("请再输入一个数字:")
        num = int(temp)

print("game over")