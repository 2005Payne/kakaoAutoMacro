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