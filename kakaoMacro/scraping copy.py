import requests
from bs4 import BeautifulSoup
from datetime import datetime
def webScraping():
    res=requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%B1%EC%9D%BC%EC%A0%95%EB%B3%B4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90+%EA%B8%89%EC%8B%9D")#요청
    html=res.text#정보가공
    soup=BeautifulSoup(html,'html.parser')#정보가공
    links=soup.select(".timeline_box")#timeline_box라는 css class선택자 검색

    today=[str(datetime.now().month),str(datetime.now().day)]#오늘 날짜
    today=['10','4']
    
    text=[]
    text.append("┌─────────┐")
    text.append(" 10월 13일 ºㅁº 냠냠이".format(today[0],today[1]))
    text.append("└─────────┘")
    text.append("　　ᕱ ᕱ  ||")
    text.append("　 (･ω･  ||")
    text.append("　 /　つΦ")
    # text.append("{0}월 {1}일 냠냠이 ºㅁº".format(today[0],today[1]))
    
    for link in links:#반복
        temp=[i for i in link.text.split(' ') if i != '']
        # print(temp)
        if(list(temp[0].split('.'))[0:2]==today):
            text.append('')
            for t in link.select(".text"):
                text.append(t.text)
            return text
        
    return "급식 정보가 없습니다." #오늘 날짜와 일치하는 정보가 없을 경우

for i in webScraping():
    print(i)