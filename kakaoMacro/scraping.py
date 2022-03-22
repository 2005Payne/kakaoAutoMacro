import requests
from bs4 import BeautifulSoup
from datetime import datetime
def webScraping():
    res=requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%B1%EC%9D%BC%EC%A0%95%EB%B3%B4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90+%EA%B8%89%EC%8B%9D")
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    links=soup.select(".timeline_box")

    today=[str(datetime.now().month),str(datetime.now().day)]
    # today=['3','10']
    for link in links:
        if list(link.text.split())[0].split('.')[0:2]==today:
            return list(link.text.split())
        
    return "급식 정보가 없습니다."
webScraping()