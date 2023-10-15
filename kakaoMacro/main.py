from datetime import datetime
from os import system
from Automatic import Macro
from scraping import webScraping
import time
import sys
# pip install requests

# pip install BeautifulSoup
# pip install bs4
# pip install pyautogui
# pip install pyperclip

setTime=840 #시는 100과 1000의 자리수에 있고 분은 1과 10의자리수에 있다 8시40분

print("매크로 실행중에는 마우스포인터가 보이지 않습니다. 안내에 따라주세요")
while(True):
    nowtime=datetime.now().hour*100+datetime.now().minute#현재 시간의 시에 100을 곱하고 분과 더하여 setTime과 같은 형태로 만듬
    if(nowtime>=setTime):#현재 시간이 setTime보다 크면서 filemode.p의 값을 읽어 '0'이면 아래 코드 실행
        print("매크로 실행 마우스를 건드리지 마세요")
        Macro.kakaoMacro(webScraping(),"성일정보고급식알림")
        # Macro.kakaoMacro(webScraping(),"박보현")
        sys.exit()
    elif(nowtime<setTime):#현재시간이 setTime보다 작으면서 filemode.p의 값이 '1'이면 아래코드 실행
        time.sleep(1)#1초 쉼