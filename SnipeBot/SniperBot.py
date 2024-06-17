from selenium import webdriver
import csv
import time
import pyautogui as py
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askquestion, askokcancel, askyesno
from PIL import ImageTk, Image
import locale
import sys
import requests
from bs4 import BeautifulSoup
import replace
import webbrowser
import keyboard as kb

def getUsername():
    global KullaniciAdi
    KullaniciAdi = entry.get()

def getPassword():
    global Sifre
    Sifre = entryPass.get()

def getTFA():
    global TFA
    TFA = TFA_entry.get()

def setDealPercent():
    global DealP
    DealP = dealPercent_entry.get()

def setRBX():
    global RBXP
    RBXP = RBXPercent_entry.get()

def Discord():
    webbrowser. open('https://discord.gg/5UenDgXq')

def show_TOU():
    askyesno(title='User Agreements', message='First of all, fill in the necessary information for your account that you want to snipe for, the data entered in line with this \n program (username and password) are not recorded in any way. It is a completely local-side program and no data is sent \n to the developer of the program. Secondly, if there is 2-factor authentication, you will have to enter it yourself.\n The program just opens roblox.com/login and logs in by entering the username and password you entered. \n If you have two-factor authentication (such as authenticator or mail verification, etc.), you need to fill them manually. \n You have 30 seconds, otherwise the program will fail. After filling in, you will enter roblox.com/home page and when \n 30 seconds (2-factor authentication period) expires, you will be redirected to site which snipe the items. \n Third and Finally, while filling out the required fields in the program, you determine the indicators you want \n (such as how many robux will be or what percentage of the deal will be), after filling everything, \n the program should run without any errors. THE DEVELOPER IS NOT RESPONSIBLE FOR ANY BANS.')

def setBuy():
    global BuyBool
    BuyBool = Buy_On.get()
    
def Start():
    print("Started")

    driver=webdriver.Firefox()

    adresRB="https://www.roblox.com/login"
    adres="https://www.rolimons.com/deals"

    driver.get(adresRB)

    KullaniciAdiX = driver.find_element("xpath", '//*[@id="login-username"]')
    KullaniciAdiX.click()
    py.write(KullaniciAdi)
    #py.click(855,437)#736,372
    #py.write(KullaniciAdi)
    #py.click(857,520)#743,450
    SifreX = driver.find_element("xpath", '//*[@id="login-password"]')
    SifreX.click()
    py.write(Sifre)
    LoginX = driver.find_element("xpath", '//*[@id="login-button"]')
    LoginX.click()
    
    BuyBool = Buy_On.get()
    print(BuyBool)
    
    def Sorgula(Url):
        global UrlSuan
        UrlSuan = driver.current_url
        print(UrlSuan)
        if UrlSuan == "https://www.roblox.com/home":
           driver.get(adres)
        elif UrlSuan == "https://www.roblox.com/my/avatar":
            driver.get(adres)
        #elif UrlSuan == UrunUrl:
            #print("ALDIM VERDIM BEN SENI YENDIM")

    if  TFA == 1:
        py.click(929,826)#798,824
        print("Dogrulama Kodunuzu Robloxtaki Gerekli Alana Yaziniz")
        
    time.sleep(30)
    Url = driver.current_url
    Sorgula(Url)

    while True:
    
        #try:
    
        #pyautogui.displayMousePosition()
 
        sys.stdout = PrintLogger(textbox)

        if kb.is_pressed("<"):
            driver.close()
            exit()
            quit()
        
        UrunAdiXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[1]/div"
        UrunFiyatiXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[3]/div[1]/div[2]"
        UrunRapXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[3]/div[2]/div[2]"
        UrunDealXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[3]/div[3]/div[2]"
        UrunDealBuyukXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[3]/div[4]/div[2]"
        #UrunUrlXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a"
        #UrunProjectedXpath="/html/body/div[2]/div[2]/div[5]/div[1]/a/div/div[3]/div[4]/span"
        UrunAdi=driver.find_element("xpath", UrunAdiXpath).text
        UrunFiyati=driver.find_element("xpath", UrunFiyatiXpath).text
        UrunRap=driver.find_element("xpath", UrunRapXpath).text
        UrunDeal=driver.find_element("xpath", UrunDealXpath).text
        UrunDealBuyuk=driver.find_element("xpath", UrunDealBuyukXpath).text
        #UrunUrl=driver.find_element("xpath", UrunUrlXpath)  
        #UrunProjected=driver.find_element("xpath", UrunProjectedXpath).text

    
            #UrunFiyatiXpath="/html/body/div[1]/div[5]/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div[i]/div[1]/a/div[2]/div[3]/div/div"
            #km=driver.find_element_by_xpath(kmadres).text

            #km=km.replace(".","")
            
            #fiyatadres="/html/body/div[2]/div[2]/div[4]/div/div[2]/div[2]/table/tbody/tr["+x+"]/td[7]/div[1]/span/a"
            #fiyat=driver.find_element_by_xpath(fiyatadres).text
            #fiyat=fiyat.replace(".","").replace(" ","").replace("TL","")

        #UrunDealInt = "".join(c for c in UrunDeal if c.isdecimal())
        #UrunDealInt2 = float(UrunDealInt.replace(',', ''))
        UrunDealBuyukInt = "".join(c for c in UrunDealBuyuk if c.isdecimal())

            
        
        #UrunFiyatiInt = "".join(c for c in UrunFiyati if c.isnumeric()) 

        try:
            UrunFiyatiFloat = float(UrunFiyati.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunFiyati ({UrunFiyati}) to a float.")
        try:
            UrunDealInt = "".join(c for c in UrunDeal if c.isdecimal())
            UrunDealInt2 = float(UrunDealInt.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunDeal ({UrunDeal}) to a float.")
            
        if (UrunDealBuyukInt) == "":
            UrunDealBuyukInt = 0
        
        if (int(float(UrunDealInt2))) >= (int(DealP)): #& int(float(UrunDealBuyukInt)) <= int(DealP):
            print("ZAAAAAA")
            if (int(float(UrunDealBuyukInt))) == 0:
                py.click(359,672)#359,672
                if (BuyBool == 1) and (UrunFiyatiFloat <= float(RBXP)):
                    #time.sleep(5)
                    py.click(1117,657)
                    py.click(903,988)
                    Url = driver.current_url
                    Sorgula(Url)
                
        try:
            UrunFiyatiFloat = float(UrunFiyati.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunFiyati ({UrunFiyati}) to a float.")

        try:
            UrunDealInt = "".join(c for c in UrunDeal if c.isdecimal())
            UrunDealInt2 = float(UrunDealInt.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunDeal ({UrunDeal}) to a float.")

        if (UrunFiyatiFloat <= float(RBXP)) and (int(float(UrunDealInt2))) >= (int(DealP)):
            print("ZUHAHAHAHA")
            py.click(359,672)#359,672
            if (BuyBool == 1):
                #time.sleep(5)
                py.click(1117,657)
                py.click(903,988)
                Url = driver.current_url
                Sorgula(Url)

        try:
            UrunFiyatiFloat = float(UrunFiyati.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunFiyati ({UrunFiyati}) to a float.")

        try:
            UrunDealInt = "".join(c for c in UrunDeal if c.isdecimal())
            UrunDealInt2 = float(UrunDealInt.replace(',', ''))
        except ValueError:
            print(f"Error: Unable to convert UrunDeal ({UrunDeal}) to a float.")

        if (int(float(UrunDealBuyukInt))) != 0 and (int(float(UrunDealBuyukInt))) >= (int(DealP)):
            print("ZJZJZJZJZJZ")
            py.click(359,672)#359,672
            if (BuyBool == 1) and (UrunFiyatiFloat <= float(RBXP)):
                    #time.sleep(5)
                    py.click(1117,657)
                    py.click(903,988)
                    Url = driver.current_url
                    Sorgula(Url)
            
        "print(ss,i,UrunAdi,km,fiyat)"
        print("Adi:", UrunAdi)
        #time.sleep(1)
        print("Fiyat:", UrunFiyati, "RBX")
        #time.sleep(1)
        print("Rap:", UrunRap)
        #time.sleep(1)
        print("Deal:", UrunDeal)
        print(UrunDealInt)
        #time.sleep(1)
        print("DealBuyuk:", UrunDealBuyuk)
        #time.sleep(1)
        #print("UrunURL:", UrunUrl)
        #print("Projected?:", UrunProjected)
        print("------------------------------------------------")
        
        #except:
            #print("ඞ")
            
                

    driver.close()    


class PrintLogger: 
    def __init__(self, textbox): 
        self.textbox = textbox 
 
    def write(self, text): 
        self.textbox.insert(tk.END, text)

window = tk.Tk()
window.title("Sniper Bot By Xenon V1.1")
window.geometry('1000x1500')
window.resizable(False, False)

title_label = ttk.Label(master = window, text = '_$NIPER V1.1_', font ='Roboto 24 bold')
#gif_label=ttk.Label(master = window)
frameCnt = 14
frames = [PhotoImage(file='3046-c-snipe.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)
label = Label(window)
#gif_label.pack()
label.pack()
label.place(x = 60)
window.after(0, update, 0)

frameCnt2 = 14
frames2 = [PhotoImage(file='3046-c-snipe.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt2)]

def update2(ind):

    frame2 = frames2[ind]
    ind += 1
    if ind == frameCnt2:
        ind = 0
    label2.configure(image=frame2)
    window.after(100, update2, ind)
label2 = Label(window)
#gif_label.pack()
label2.pack()
label2.place(x = 810)
window.after(0, update2, 0)
title_label.pack()


img = PhotoImage(file='1Snipe.png')
Label(window,image=img).pack(pady=50)



input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Ok', command = getUsername)
input_label = ttk.Label(master = input_frame, text = 'Your Roblox Username', font = 'Helvetica 12 underline')
button.pack(side='right')
entry.pack(side = 'right', padx = 20)
input_label.pack(side = 'right')
input_frame.pack()

pass_frame = ttk.Frame(master = window)
entryPass = ttk.Entry(master = pass_frame, show="♥")
buttonPass = ttk.Button(master = pass_frame, text = 'Ok', command = getPassword)
pass_label = ttk.Label(master = pass_frame, text = 'Your Roblox Password', font = 'Helvetica 12 underline')
buttonPass.pack(side='right')
entryPass.pack(side = 'right', padx = 20)
pass_label.pack(side = 'right', pady = 20)
pass_frame.pack()

TFA_frame = ttk.Frame(master = window)
TFA_entry = ttk.Entry(master = TFA_frame)
TFA_button = ttk.Button(master = TFA_frame, text = 'Ok', command = getTFA)
TFA_label = ttk.Label(master = TFA_frame, text = 'Does Your Account Have Two-Factor Authentication (1/0)', font = 'Helvetica 12 underline')
TFA_button.pack(side = 'right')
TFA_entry.pack(side = 'right', padx = 10)
TFA_label.pack(side = 'right', pady = 20)
TFA_frame.pack()


Indiframe = ttk.Frame(master = window)
Indilabel = ttk.Label(master = Indiframe, text = '--------INDICATORS--------', font = 'Roboto 15 bold')
Indilabel.pack()
Indiframe.pack()

dealPercent_frame = ttk.Frame(master = window)
dealPercent_entry = ttk.Entry(master = dealPercent_frame)
dealPercent_button = ttk.Button(master = dealPercent_frame, text = 'Set', command = setDealPercent)
dealPercent_label = ttk.Label(master = dealPercent_frame, text = 'How much deal you want to snipe', font = 'Helvetica 12 underline bold')
dealPercent_button.pack(side = 'right')
dealPercent_entry.pack(side = 'right', padx = 20)
dealPercent_label.pack(side = 'right', pady = 20)
dealPercent_frame.pack()

RBXPercent_frame = ttk.Frame(master = window)
RBXPercent_entry = ttk.Entry(master = RBXPercent_frame)
RBXPercent_button = ttk.Button(master = RBXPercent_frame, text = 'Set', command = setRBX)
RBXPercent_label = ttk.Label(master = RBXPercent_frame, text = 'Max robux amount of the item you want to snipe', font= 'Helvetica 12 underline bold')
RBXPercent_button.pack(side = 'right')
RBXPercent_entry.pack(side = 'right', padx = 20)
RBXPercent_label.pack(side = 'right', pady = 20)
RBXPercent_frame.pack()
"""
CoordsX_frame = ttk.Frame(master = window)
CoordsX_entry = ttk.Entry(master = CoordsX_frame)
CoordsX_button = ttk.Button(master = CoordsX_frame, text = 'Set', command = setClickX)
CoordsX_label = ttk.Label(master = CoordsX_frame, text = 'Sets the clicking X coordinate (empty for defult)', font= 'Helvetica 12 underline bold')
CoordsX_button.pack(side = 'right')
CoordsX_entry.pack(side = 'right', padx = 20)
CoordsX_label.pack(side = 'right', pady = 20)
CoordsX_frame.pack()

CoordsY_frame = ttk.Frame(master = window)
CoordsY_entry = ttk.Entry(master = CoordsY_frame)
CoordsY_button = ttk.Button(master = CoordsY_frame, text = 'Set', command = setClickY)
CoordsY_label = ttk.Label(master = CoordsY_frame, text = 'Sets the clicking Y coordinate (empty for defult)', font= 'Helvetica 12 underline bold')
CoordsY_button.pack(side = 'right')
CoordsY_entry.pack(side = 'right', padx = 20)
CoordsY_label.pack(side = 'right', pady = 20)
CoordsY_frame.pack()
"""

Buy_frame = ttk.Frame(master = window)
Buy_On = IntVar()
Buy_label = ttk.Label(master = Buy_frame, text = 'Buy?(Check On/Unchecked Off)', font = "Helvetica 12 underline bold")
Buy_check = ttk.Checkbutton(master = Buy_frame, variable = Buy_On, command = setBuy)
Buy_label.pack(side ='left')
Buy_check.pack(side = 'left', pady = 20)
Buy_frame.pack()

Start_frame = ttk.Frame(master = window)
Start_button = ttk.Button(master = Start_frame, text = '▄︻デ══━一', command = Start, width = 40)
Start_label = ttk.Label(master = Start_frame, text = 'PRESS BUTTON TO START SNIPING', font = 'Roboto 20 bold')
Start_label.pack()
Start_button.pack(pady=20)
Start_frame.pack()

Press_frame = ttk.Frame(master = window)
Press_label = ttk.Label(master = Press_frame, text = 'Press < to close sniper', font = 'Helvetica 12')
Press_label.pack()
Press_frame.pack()


TOU_frame = ttk.Frame(master = window)
TOU_button = ttk.Button(master = TOU_frame, text ='User Agreements Click',width = 40 ,command = show_TOU,)
TOU_label = ttk.Label(master = TOU_frame, text = 'You must read and accept the Terms Of Uses (User Agreements) \n When you use the script, you accept the User Agreement.', font = 'Helvetica 15 bold')
TOU_label.pack()
TOU_button.pack()
TOU_frame.pack(pady=50)

photo = PhotoImage(file = "discord3.png")
Credentials_frame = ttk.Frame(master = window)
Credentials_label = ttk.Label(master = Credentials_frame, text = 'Developed By Xenon', font = 'Helvetica 13 italic')
Credentials_dc = ttk.Label(master = Credentials_frame, text = 'Discord: ixenon_', font = 'Helvetica 11 italic bold')
Credentials_Dcs = ttk.Button(master = Credentials_frame, image = photo, width = 10, command = Discord)
Credentials_label.pack()
Credentials_dc.pack()
Credentials_Dcs.pack()
Credentials_frame.pack(pady = 30)


textbox = tk.Text(window) 
textbox.pack() 



window.mainloop()



#KullaniciAdi = input("Kullanici Adinizi Girinizz: ")

#Sifre = input("Sifrenizi Giriniz: ")

#TFA = int(input("Iki faktörlü Dogrulama var mi (1/0): "))







