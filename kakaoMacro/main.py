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

