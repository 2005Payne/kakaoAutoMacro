import pyautogui
import time
import pyperclip
#locateOnScreen
class Macro:

    # def imgClick(imgtext):
    #     i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))#이미지에 해당하는 곳의 가운데 위치를 저장
    #     while(i==None):#i가 값이 안들어가면 이미지를 못찾았다는 뜻으로 계속 반복하여 찾음
    #         i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))
        # pyautogui.click(i) #클릭
    # def sleepClick(second):
    #     pyautogui.click()
    #     time.sleep(second)#second초 만큼 쉼

    def cV(text):
        pyperclip.copy(text)#한영키를 눌렀는지 안눌렀는지에 따라 값이 바뀌는 경우가 생겨서 클립보드를 이용함
        pyautogui.hotkey("ctrl", "v") #붙여넣기

    def openKakao():
        pyautogui.press('win')
        time.sleep(0.2)
        pyautogui.write("w")
        pyautogui.press("backspace")
        time.sleep(0.2)
        Macro.cV("카카오톡")
        pyautogui.press("enter")
    def passwordKakao():
        # i=pyautogui.locateCenterOnScreen('img/password.png')
        # while(i==None):
        #     i=pyautogui.locateCenterOnScreen('img/password.png')
        #     if(i==None):
        #         i=pyautogui.locateCenterOnScreen('img/password2.png')
        # pyautogui.click(i)
        time.sleep(5)
        Macro.cV("wo2487@45")
        pyautogui.press("enter")
    def printKakao(text,mode): #여기서 text는 카카오톡에 메시지 보낼때 값입니다 mode는 보낼 대상이름 입니다.
        time.sleep(1)
        pyautogui.hotkey("ctrl", "f")
        time.sleep(0.5)
        Macro.cV(mode)
        time.sleep(0.5)
        pyautogui.press("enter")
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
        pyautogui.hotkey("alt", "n")
        pyautogui.press("esc")
    def kakaoMacro(text,mode):
        pyautogui.press("enter")
        pyautogui.press("esc")
        Macro.openKakao()
        time.sleep(20)
        Macro.passwordKakao()
        time.sleep(1)
        Macro.printKakao(text,mode)
        # pyautogui.hotkey("win","r")
        # time.sleep(1)
        # Macro.cV("cmd")
        # time.sleep(1)
        # pyautogui.press("enter")
        # time.sleep(1)
        # Macro.cV("shutdown -s")
        # pyautogui.press("enter")