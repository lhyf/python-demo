# sum = 0
# for i in range(1, 101):
#     sum = sum + i
#
# print(sum)
# sum = '1'
# print(sum)

class a():
    def sayhello(self,name):
        print("hello "+name+"!")
        return self

b=a()
c=b.sayhello("lita")
print(b==c)