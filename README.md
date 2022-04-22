# kakaoAutoMacro
<html>
  <body>
    이 프로그램은 카톡을 키는것부터 인터넷에서 스크래핑해온것을 원하는 곳에 보내준 다음 로그아웃까지 해주는 프로그램입니다.
    아래 영상에서 로그아웃 하고 이후에 움직이는 것은 오늘 급식이 맞는지 스크래핑제대로 한게 맞은지 확인을 위해서
    제가 움직인 것입니다.<br>
    <a href="https://user-images.githubusercontent.com/88232976/164607475-e88feab9-2db1-4923-96fe-394171416657.mp4">실행영상보러가기</a>
    코드보기<br>
    --------main---------
    <python>
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
def openfile(mode,text):
    with open("filemode.p","{}".format(mode)) as f:
        if mode=='w':
            f.write(text)
        elif mode=='r':
            return f.read()

setTime=840

mode=openfile('r','')
print("매크로 실행중에는 마우스포인터가 보이지 않습니다. 안내에 따라주세요")
while(True):
    nowtime=datetime.now().hour*100+datetime.now().minute
    if(nowtime>=setTime and openfile("r",'')=='0'):
        print("매크로 실행 마우스를 건드리지 마세요")
        Macro.kakaoMacro(webScraping(),"박재우")
        openfile("w",'1')
        sys.exit()
    elif(nowtime<setTime and openfile("r",''
    )=="1"):
        openfile("w",'0')
        print("파일 초기화")
        time.sleep(1)
    </python>


    <br>
    --------스크래핑---------<br>
    <img herf="https://user-images.githubusercontent.com/88232976/164608024-aad3516e-c8cf-4991-a2a3-a49e0fa31ca2.png">
    <br>
    -------매크로------------<br>
    <img herf=https://user-images.githubusercontent.com/88232976/164608093-c795bfde-19e5-4ff2-a0af-cb7fc5cb2054.png">
    <br>
    <img herf=https://user-images.githubusercontent.com/88232976/164608128-382d8966-86f7-443e-a768-d9468943a1a0.png">

  </body>
</html>

