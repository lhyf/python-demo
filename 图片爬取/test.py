import re

#content = '<img alt="晴日下的美少女-唯美女生" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="801" height="1200" class="alignnone size-full wp-image-6479" data-src="https://static.vmgirls.com/image/2018/03/2018-03-07_14-01-27.jpg" data-nclazyload="true" data-srcset="https://static.vmgirls.com/image/2018/03/2018-03-07_14-01-27.jpg 801w, https://static.vmgirls.com/image/2018/03/2018-03-07_14-01-27-684x1024.jpg 684w" data-sizes="(max-width: 801px) 100vw, 801px">'
#content = '<img alt="甜甜的，这时光-唯美女生" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="https://static.vmgirls.com/image/2019/06/2019-06-13_02-25-28.jpg" data-nclazyload="true">'
content = '<img alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="avatar avatar-40 photo w-40" height="40" width="40" data-src="//gravatar.loli.net/avatar/33f65a8b2e6b32e66a4d99d8592d9b6e?s=40&amp;d=https%3A%2F%2Fwww.vmgirls.com%2Fimage%2F2019%2F02%2FIMG_54681.jpg&amp;r=g" data-nclazyload="true" data-srcset="//gravatar.loli.net/avatar/33f65a8b2e6b32e66a4d99d8592d9b6e?s=80&amp;d=https%3A%2F%2Fwww.vmgirls.com%2Fimage%2F2019%2F02%2FIMG_54681.jpg&amp;r=g 2x">'
list = re.findall('<img .*? data-src="(.*?)" data-nclazyload="true" .*?>',content)
# list = re.findall('<img alt=".*?" src=".*?" class=".*?" data-src="(.*?)" data-nclazyload="true">',content)
print(list)
print(len(list))
