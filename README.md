# kakaoAutoMacro

```python
#--------main--------
from datetime import datetime
from os import system
from Automatic import Macro
from scraping import webScraping
import time
import sys
#pip install pillow
#pip install requests
#pip install BeautifulSoup
#pip install bs4
#pip install pyautogui
#pip install pyperclip
#pip install pyinstaller

def openfile(mode,text):#filemode.p를 mode에 따라 읽거나,내용을 바꿀지 정함
    with open("filemode.p","{}".format(mode)) as f:
        if mode=='w':
            f.write(text)
        elif mode=='r':
            return f.read()

setTime=840 #시는 100과 1000의 자리수에 있고 분은 1과 10의자리수에 있다 8시40분

mode=openfile('r','')
print("매크로 실행중에는 마우스포인터가 보이지 않습니다. 안내에 따라주세요")
while(True):
    nowtime=datetime.now().hour*100+datetime.now().minute#현재 시간의 시에 100을 곱하고 분과 더하여 setTime과 같은 형태로 만듬
    if(nowtime>=setTime and openfile("r",'')=='0'):#현재 시간이 setTime보다 크면서 filemode.p의 값을 읽어 '0'이면 아래 코드 실행
        print("매크로 실행 마우스를 건드리지 마세요")
        Macro.kakaoMacro(webScraping(),"박재우")#Automatic스크립트파일에 Macro 라는 클래스의 kakaoMacro라는 함수를 실행 scraping파일에 webScraping이라는 함수와, "박재우"를 인자로 사용
        openfile("w",'1')#filemode.p의 값을 1로바꿔 하루에 1번만 실행되게 설정
        sys.exit()#프로그램을 종료
    elif(nowtime<setTime and openfile("r",'')=="1"):#현재시간이 setTime보다 작으면서 filemode.p의 값이 '1'이면 아래코드 실행
        openfile("w",'0') #filemode.p의 값을 0으로 바꿈
        print("파일 초기화")
        time.sleep(1)#1초 쉼
```
```python
#-------Automatic----
import pyautogui
import time
import pyperclip
#locateOnScreen
class Macro:
    #메크로는 노가다 작업이라서 중복되는것은 넣지 않았습니다.
    #그리고 메소드를 나눠서 만든 이유는 처음 만든 main은 tkinter을 이용하여 버튼을 누르면 실행하는 방식이여서
    #로그인이 되어있는 상태에서 실행할 수 있는 버튼을 만들었기 때문입니다.
    def imgClick(imgtext):
        i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))#이미지에 해당하는 곳의 가운데 위치를 저장
        while(i==None):#i가 값이 안들어가면 이미지를 못찾았다는 뜻으로 계속 반복하여 찾음
            i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))
        pyautogui.click(i) #클릭
    def sleepClick(second):
        pyautogui.click()
        time.sleep(second)#second초 만큼 쉼

    def cV(text):
        pyperclip.copy(text)#한영키를 눌렀는지 안눌렀는지에 따라 값이 바뀌는 경우가 생겨서 클립보드를 이용함
        pyautogui.hotkey("ctrl", "v") #붙여넣기

    def openKakao():
        pyautogui.click(26,1055)
        time.sleep(0.2)
        pyautogui.write("w")
        pyautogui.press("backspace")
        time.sleep(0.2)
        Macro.cV("카카오톡")
        pyautogui.press("enter")
    def passwordKakao():
        i=pyautogui.locateCenterOnScreen('img/password.png')
        while(i==None):
            i=pyautogui.locateCenterOnScreen('img/password.png')
            if(i==None):
                i=pyautogui.locateCenterOnScreen('img/password2.png')
        pyautogui.click(i)
        Macro.cV("**********************************")#비밀번호는 개인정보라서 가렸씁니다.
        pyautogui.press("enter")

    def printKakao(text,mode): #여기서 text는 카카오톡에 메시지 보낼때 값입니다 mode는 보낼 대상이름 입니다.
        time.sleep(1)
        Macro.imgClick("kakao")
        Macro.imgClick("search")
        time.sleep(0.5)
        Macro.cV(mode)
        time.sleep(1)
        pyautogui.moveRel(0,120)
        pyautogui.doubleClick()
        time.sleep(1)
        for i in text:
            if "TODAY"!=i:#스크래핑해온 값을 보면 오늘 급식인 것에 TODAY라고 써있기 그것을 뺴기 위한 조건문
                pyperclip.copy(i)
                pyautogui.hotkey("ctrl","v")
                pyautogui.hotkey("shift","enter")
                time.sleep(0.1)
        pyautogui.press("backspace")
        pyautogui.press("enter")
        pyautogui.press("esc")
        Macro.imgClick("exit1")
        Macro.imgClick("exit2")
        pyautogui.press("esc")
    def kakaoMacro(text,mode):
        pyautogui.press("enter")
        pyautogui.press("esc")
        Macro.openKakao()
        time.sleep(10)
        Macro.passwordKakao()
        time.sleep(1)
        Macro.printKakao(text,mode)
```
```python
#-------scraping-----
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
```
이 프로그램은 카톡을 키는것부터 인터넷에서 스크래핑해온것을 원하는 곳에 보내준 다음 로그아웃까지 해주는 프로그램입니다.
아래 영상에서 로그아웃 하고 이후에 움직이는 것은 오늘 급식이 맞는지 스크래핑이 정상작동 확인을 위해서
매크로가 아닌 제가 네이버에 성일정보고급식을 검색한 것입니다.<br>
<a href="https://user-images.githubusercontent.com/88232976/164607475-e88feab9-2db1-4923-96fe-394171416657.mp4">실행영상보러가기</a>
<a href="https://open.kakao.com/o/gi9uU24d">급식 알림(카카오톡 오픈채팅방)</a>
