import scraping
import Automatic
import tkinter as tk
#pip install pillow
#pip install requests
#pip install BeautifulSoup
#pip install bs4
#pip install pyautogui
#pip install pyperclip
#pip install pyinstaller
def kakaoCommand(mode):
    if mode==1:
        Automatic.Macro.kakaoMacro(scraping.webScraping(),"박재우")
    if mode==2:
        Automatic.Macro.openKakao()
        Automatic.Macro.printKakao(scraping.webScraping(),"쌤 반톡")
root=tk.Tk()
root.geometry("400x90-0+0")
btn1=tk.Button(root,text="로그인 실행" ,command=lambda:kakaoCommand(1))
btn2=tk.Button(root,text="로그인 하지않고 실행",command=lambda:kakaoCommand(2))
btn1.pack()
btn2.pack()
root.mainloop()