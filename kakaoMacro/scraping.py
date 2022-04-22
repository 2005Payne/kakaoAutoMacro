import requests
from bs4 import BeautifulSoup
from datetime import datetime
def webScraping():
    res=requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%B1%EC%9D%BC%EC%A0%95%EB%B3%B4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90+%EA%B8%89%EC%8B%9D")#요청
    html=res.text#정보가공
    soup=BeautifulSoup(html,'html.parser')#정보가공
    links=soup.select(".timeline_box")#timeline_box라는 css class선택자 검색

    today=[str(datetime.now().month),str(datetime.now().day)]#오늘 날짜
    for link in links:#반복
        if list(link.text.split())[0].split('.')[0:2]==today:#오늘 날짜와 일치하는 정보를
            return list(link.text.split())#리턴함
        
    return "급식 정보가 없습니다." #오늘 날짜와 일치하는 정보가 없을 경우