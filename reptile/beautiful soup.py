import requests
from bs4 import BeautifulSoup

"""
<html>
 <head>
  <title>This is a python demo page</title>
 </head> 
 <body> 
  <p class="title"><b>The demo python introduces several python courses.</b></p> 
  <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses: <a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p> 
 </body>
</html>
"""
r = requests.get("https://python123.io/ws/demo.html")
content = r.text

soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())

print("*" * 60)

# 获取 head 标签
print(soup.head) #<head><title>This is a python demo page</title></head>

# 获取标签名
print(soup.head.name) #head

# 获取 p 标签属性,返回值为一个 字典
print(soup.p.attrs) #{'class': ['title']}

# 获取 title 标签中的内容
print(soup.title.string) #This is a python demo page


for link in soup.find_all("a"):
    print(link.get('href'))
