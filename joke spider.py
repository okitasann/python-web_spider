from bs4 import BeautifulSoup
import requests
def webspider(url):
    useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36"
    header = {'User-Agent': useragent}
    request=requests.get(url,headers=header)
    data=request.content
    return data
def txtproducer(list):
    with open("txt.txt","a") as f:
        for line in list:
            f.write(line)
def textsniffer(url):
    soup=BeautifulSoup(url,"html.parser")
    text=[]
    listitem=soup.find_all("div",attrs={"class":"joke-list-item"})
    article=[]
    for one in listitem:
       for two in one.find_all("a",attrs={"class":"inline-block joke-user-info-nickname"}):
            userinfo=two.get_text()+":"
            article.append(userinfo)
            txtproducer(userinfo)
            txtproducer("\n")
            for three in one.find_all("div",attrs="joke-main-content clearfix"):
                if "joke-main-img" in three:
                    img=three.img["src"]
                    article.append(img)
                    txtproducer(img)
                    txtproducer("\n")
                content = three.p.get_text()
                article.append(content)
                txtproducer(content)
                txtproducer("\n")
    return article
if __name__=="__main__":
    html=webspider("http://www.haha.mx/new")
    temp=textsniffer(html)
    print(temp)
