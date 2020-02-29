# file_name = "C:/Users/LHYF/Desktop/专辑/幼教亲宝儿歌.rar"
file_name = "F:/迅雷下载/我的天才女友.My.Brilliant.Friend.S01E01.中英字幕.WEB.1080p-人人影视.mp4"

file_new_name = "F:/迅雷下载/我的天才女友.My.Brilliant.Friend.S01E01.中英字幕.WEB.1080p.mp4"
with open(file_name, "rb") as file_obj:
    with open(file_new_name, 'wb') as file_obj2:
        while True:
            chunk = 1024
            content = file_obj.read(chunk)
            file_obj2.write(content)

            file_obj.seek(1024,1)
            # 显示当前读取的位置
            print(file_obj.tell())

            if not content:
                break
