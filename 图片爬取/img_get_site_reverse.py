import requests
import re
import pprint
import os
import time

headers = {
    "user-agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


def get_all_page_list(url):
    """
    获取站点所有页面列表
    :param url: 站点连接
    :return:
    """
    xml_content = get_page_html(url)
    # 获取所有页面地址
    url_list = re.findall("<loc>(.*?)</loc>", xml_content)
    return url_list


def get_site_map_url_list(url):
    """
    获取站点地图中的图片列表
    :return:
    """
    content = get_page_html(url)

    url_list = re.findall('<a href="(.*?)" title=".*?" target="_blank">', content)
    return url_list


def get_img_url(url):
    """
    获取一系列页面html内容,包含下一页
    :param url: 第一页页面链接
    :return: imgs: 系列页面下的图片列表,dir_name:系列页面title
    """
    # 获取到主页面
    content = get_page_html(url)
    if not content:
        return {'imgs': '', 'dir_name': '页面获取错误'}

    # 获取当前页面图片连接
    imgs = get_page_img_url(content)
    # 获取页面名称
    dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', content)[-1]

    # 获取到页面包含的下一页列表
    next_page_list = re.findall('<a href="(.*?)" class="post-page-numbers">', content)

    # 循环获取下一页的图片列表
    for next in next_page_list:
        content = get_page_html(next)
        if not content:
            continue

        # 获取当前页面图片连接
        img = get_page_img_url(content)
        imgs.update(img)

    return {'imgs': imgs, 'dir_name': dir_name}


def get_page_html(url):
    """
    返回单个页面html内容
    :param url:
    :return:
    """
    try:
        print(f"当前获取页面:{url}")
        response = requests.get(url, headers=headers,timeout=30)
        response.raise_for_status()
        content = response.text
        return content
    except:
        print(f"页面获取失败:{url}")


def get_page_img_url(html_content):
    """
    获取图片列表
    :param html_content:
    :return:
    """
    # urls = re.findall('<img alt=".*?" src=".*?" class=".*?" data-src="(.*?)" data-nclazyload="true">',
    #                   html_content)
    urls = re.findall('<img .*? data-src="(.*?)" .*?>',
                      html_content)
    urls2 = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html_content)

    imgs = set(urls)
    imgs.update(urls2)
    return imgs


def save_img(dir_name, imgs):
    """
    保存图片到 dir_name 文件夹,如果图片已经存在,则跳过
    :param dir_name:
    :param imgs:
    :return:
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        print("文件夹已存在: %s"%dir_name)
    for url in imgs:
        # 获取图片名字
        file_name = url.split("/")[-1]
        if not os.path.exists(dir_name + "/" + file_name):
            print(f'当前获取图片名:{file_name}')
            try:
                img = requests.get(url, headers=headers,timeout=30)
                with open(dir_name + "/" + file_name, "wb") as img_obj:
                    img_obj.write(img.content)
            except:
                print(f"下载图片错误 {url}")
        else:
            print("图片已存在: %s" % file_name)


# site_url = "https://www.vmgirls.com/sitemap-image.xml"
# url_list = get_all_page_list(site_url)

site_map_url = "https://www.vmgirls.com/sitemap.shtml"
url_list = get_site_map_url_list(site_map_url)
# 翻转列表
url_list.reverse()

print("需要访问的页面列表:")
pprint.pprint(url_list)
print("共需获取页面", len(url_list))
print("**" * 30)

for url in url_list:
    ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 获取页面上的图片和标题
    page_info = get_img_url(url)

    # 获取到图片列表
    imgs = page_info.get("imgs")
    # 获取到页面标题
    dir_name = page_info.get("dir_name")

    print("*" * 30)
    print(f" {ticks} 开始保存图片:{dir_name}  {url}")

    save_img(dir_name, imgs)

    print("*" * 30, end="\n\n")
