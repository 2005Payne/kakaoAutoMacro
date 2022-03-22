from datetime import datetime
from Automatic import Macro
from scraping import webScraping
import time
import sys
def openfile(mode,text):
    with open("mode.p","{}".format(mode)) as f:
        if mode=='w':
            f.write(text)
        elif mode=='r':
            return f.read()
setTime=9
mode=openfile('r','')
print("매크로 실행중에는 마우스포인터가 보이지 않습니다. 안내에 따라주세요")
nowtime=int(str(datetime.now().time())[0:2])
if(int(nowtime)>=setTime and openfile("r",'')=='0'):
    print("매크로 실행 마우스를 건드리지 마세요")
    Macro.kakaoMacro(webScraping(),"성일정보고급식알림")
    Macro.kakaoMacro(webScraping(),"쌤 반톡")
    openfile("w",'1')
elif(nowtime<setTime and openfile("r",'')):
    openfile("w",'0')
    print("파일 초기화")
print("실행종료됨",nowtime)

sys.exit()