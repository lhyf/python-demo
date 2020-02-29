import time

for i in range(100):
    time.sleep(1)

    print("\r当前速度: {:.2f}%".format(i * 100 / 100), end="")
