import requests
from bs4 import BeautifulSoup
import bs4


def get_pag_html(url):
    """获取需要爬取页面HTML"""
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("获取页面失败:{}".format(e))
        return ""


def get_univ_list_form_html(html):
    """从 HTML 页面返回大学排名列表"""
    univ_list = []

    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all("td")
            univ_list.append([tds[0].string, tds[1].string, tds[3].string])

    return univ_list


def print_univ_list(list, num):
    """打印前 num 个学校"""
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "分数",chr(12288)))
    for i in range(num):
        print(tplt.format(list[i][0], list[i][1], list[i][2],chr(12288)))


if __name__ == '__main__':
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = get_pag_html(url)
    univ_list = get_univ_list_form_html(html)
    print_univ_list(univ_list, 10)
