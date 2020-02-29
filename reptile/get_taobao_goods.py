import requests
import re


def get_url_html(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def get_goods_list(goods_list, content):
    try:
        plt = re.findall(r'\"view_price\":\"[\d\.]*\"', content)
        tlt = re.findall(r'\"raw_title\":\".*?\"', content)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            goods_list.append([price, title])
    except:
        print("")


def print_goods_list(goods_list):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for goods in goods_list:
        count += 1
        print(tplt.format(count, goods[0], goods[1]))


def test1():
    goods = "口罩"
    dept = 2
    url = "https://s.taobao.com/search?q=" + goods

    goods_list = []
    for i in range(dept):
        content = get_url_html(url + "&s=" + str(44 * i))
        get_goods_list(goods_list, content)

    print_goods_list(goods_list)

def test2():
    with open("tt.html",'r',encoding="UTF-8") as f:
        goods_list = []
        get_goods_list(goods_list, f.read())
        print_goods_list(goods_list)

if __name__ == '__main__':
    # test1()
    test2()