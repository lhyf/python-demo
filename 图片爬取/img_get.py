import requests
import re
import pprint
import os

"""获取页面"""
headers = {
    "user-agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
response = requests.get(" https://www.vmgirls.com/3776.html", headers=headers)
content = response.text

# pprint.pprint(content)

print(content)

"""获取图片列表"""
urls = re.findall('<img alt=".*?" src=".*?" class="alignnone size-full" data-src="(.*?)" data-nclazyload="true">',
                  content)
urls2 = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', content)

imgs = set(urls)
imgs.update(urls2)

# 打印获取到的图片url
pprint.pprint(imgs)

"""保存图片"""
print("**" * 30)

# 获取页面名称
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', content)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for url in imgs:
    # 获取图片名字
    file_name = url.split("/")[-1]
    print(f'当前获取图片名:{file_name}')
    img = requests.get(url, headers=headers)
    with open(dir_name + "/" + file_name, "wb") as img_obj:
        img_obj.write(img.content)
