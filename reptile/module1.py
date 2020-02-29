import requests
import pprint


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        # 自动根据返回状态抛出异常
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(f"发生了异常: {e}")


if __name__ == "__main__":
    url = "http://www.lhyf.org"
    # content = get_html(url)
    # pprint.pprint(content)

    kv = {"k1": "v1", "k2": "v2"}
    r = requests.request("get", url, params=kv)
    print(r.url)  # http://www.lhyf.org/?k1=v1&k2=v2

    r = requests.request("POST", url, data=kv)

    print(r.url)

    body = "text"
    r = requests.request("POST", url, data=body)
    print(r.url)

    fs = {"file":open("demo.txt","rb")}
    requests.request("POST",url,files=fs)

    pxs = {"http":"http://www.baidu.com","https":"https://www.baidu.com"}
    requests.request("POST", url, proxies=pxs)

    url = 'http://ip138.com/iplookup.asp'
    kv = {'ip':'185.199.110.153','action':'2'}
    r = requests.request(url,params=kv)
    print(r.status_code)
    print(r.text)