import re
import requests
from bs4 import BeautifulSoup
def webCrawler(url):
    useragent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36"
    header={'User-Agent':useragent}
    request=requests.get(url,headers=header)
    data=request.content
    return data
def imgsniffer(url):
    regex=re.compile(r"http://[\w./]+?.jpg")
    imgGet =re.findall(regex,str(url))
    num=1
    print(imgGet)
    for img in imgGet :
        print(img)
        image=webCrawler(img)
        with open("%s.jpg"%num,"wb") as tmp:
            tmp.write(image)
            num+=1
            print("正在抓取第%s张图片"%num)
    print("图片下载完成")
    return
targetPath = "E:\\temp"
url = "http://bbs.feng.com/"
html=webCrawler(url)
imgsniffer(html)