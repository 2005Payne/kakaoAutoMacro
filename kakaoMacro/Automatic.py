import pyautogui
import time
import pyperclip
#locateOnScreen
class Macro:
    def imgClick(imgtext):
        i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))
        while(i==None):
            i=pyautogui.locateCenterOnScreen('img/{}.png'.format(imgtext))
        pyautogui.click(i)
    def sleepClick(second):
        pyautogui.click()
        time.sleep(second)

    def cV(text):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    def openKakao():
        pyautogui.click(26,1055)
        time.sleep(0.2)
        pyautogui.write("w")
        pyautogui.press("backspace")
        time.sleep(0.2)
        # pyautogui.click(98,1022)
        Macro.cV("카카오톡")
        pyautogui.press("enter")
    def passwordKakao():
        i=pyautogui.locateCenterOnScreen('img/password.png')
        while(i==None):
            i=pyautogui.locateCenterOnScreen('img/password.png')
            if(i==None):
                i=pyautogui.locateCenterOnScreen('img/password2.png')
        pyautogui.click(i)


        Macro.cV(비밀번호)

        
        pyautogui.press("enter")

    def printKakao(text,mode):
        time.sleep(1)
        Macro.imgClick("kakao")
        Macro.imgClick("search")
        time.sleep(0.5)
        # Macro.cV("성일정보고급식알림")
        Macro.cV(mode)
        time.sleep(1)
        pyautogui.moveRel(0,120)
        pyautogui.doubleClick()
        time.sleep(1)
        for i in text:
            if "TODAY"!=i:
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