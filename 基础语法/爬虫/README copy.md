在Python3中，可以使用urllib.request和requests进行网页爬取。
爬完之后提取有用的信息, 提取的方法有很多，例如使用正则表达式、Xpath、Beautiful Soup等

静态网站直接拿数据提取就行, 动态网站一般会有很多反爬虫验证套路,需要一步步分析处理才能拿到数据


1. urllib库是python内置的，无需我们额外安装，只要安装了Python就可以使用这个库。
2. requests库是第三方库，需要我们自己安装。

## requests, Beautiful Soup
https://requests.readthedocs.io/zh_CN/latest/

```cmd
pip install requests
pip install beautifulsoup4
```

http://hq.sinajs.cn/list=sh000016

