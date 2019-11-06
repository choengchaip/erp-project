import tkinter as tk
import datetime
import os
from tkinter import messagebox
import win32print, win32ui, win32con
import requests
##f = open('employees.txt', 'w')


root = tk.Tk()

canvas = tk.Canvas(root,width = 1280,height=720)
canvas.pack()

img = tk.PhotoImage(file='gif/bg.gif')
btn1 = tk.PhotoImage(file='gif/btn1.gif')
btn2 = tk.PhotoImage(file='gif/btn2.gif')
btn3 = tk.PhotoImage(file='gif/btn3.gif')
btn4 = tk.PhotoImage(file='gif/btn4.gif')

type1 = []
type2 = []
type3 = []
type4 = []

ip = "172.20.10.14"


def sendToPrinter(data):
    X=0; Y=10
    multi_line_string = data.splitlines()  
    hDC = win32ui.CreateDC ()
    ### Set default printer from Windows:
    hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
    hDC.StartDoc ("dfs")
    hDC.StartPage ()
    for line in multi_line_string:
         hDC.TextOut(X,Y,line)
         Y += 100
    hDC.EndPage ()
    hDC.EndDoc ()
    

def queueType1():
    url = "http://"+ip+":8400/getQueue"
    query = {'type':'ฝากเงิน/ถอนเงิน'}
    r = requests.get(url=url, params=query)
    jsonData = r.json()
    print(jsonData)
    data = ""
    queueId = len(type1) +1
    type1.append(queueId)
    data += ("คิว ฝากเงิน/ถอนเงิน\n")
    data += ("Now : "+ jsonData['date'] +"\n")
    data += ("Queue before you : " + str(jsonData['before']) +"\n")
    data += ("Your queue id : " + str(jsonData['id']) +"\n")
    sendToPrinter(data)
    
    
def queueType2():
    url = "http://"+ip+":8400/getQueue"
    query = {'type':'โอนเงิน'}
    r = requests.get(url=url, params=query)
    jsonData = r.json()
    print(jsonData)
    data = ""
    queueId = len(type2) +1
    type2.append(queueId)
    data += ("คิว โอนเงิน\n")
    data += ("Now : "+ jsonData['date'] +"\n")
    data += ("Queue before you : " + str(jsonData['before']) +"\n")
    data += ("Your queue id : " + str(jsonData['id']) +"\n")
    sendToPrinter(data)

def queueType3():
    url = "http://"+ip+":8400/getQueue"
    query = {'type':'เปิดบัญชีใหม่'}
    r = requests.get(url=url, params=query)
    jsonData = r.json()
    print(jsonData)
    data = ""
    queueId = len(type3) +1
    type3.append(queueId)
    data += ("คิว เปิดบัญชีใหม่\n")
    data += ("Now : "+ jsonData['date'] +"\n")
    data += ("Queue before you : " + str(jsonData['before']) +"\n")
    data += ("Your queue id : " + str(jsonData['id']) +"\n")
    sendToPrinter(data)

def queueType4():
    url = "http://"+ip+":8400/getQueue"
    query = {'type':'อื่นๆ'}
    r = requests.get(url=url, params=query)
    jsonData = r.json()
    print(jsonData)
    data = ""
    queueId = len(type4) +1
    type4.append(queueId)
    data += ("คิว อื่นๆ\n")
    data += ("Now : "+ jsonData['date'] +"\n")
    data += ("Queue before you : " + str(jsonData['before']) +"\n")
    data += ("Your queue id : " + str(jsonData['id']) +"\n")
    sendToPrinter(data)



frame = tk.Frame(root,bg="red")
frame.place(relwidth=1,relheight=1)

bg = tk.Label(frame,image=img,bd=0,highlightthickness = 0).place(relheight=1,relwidth=1)

button1 = tk.Button(frame,image=btn1,bd=0,highlightthickness = 0,command=queueType1)
button1.place(relx=0.29,rely=0.35)
button2 = tk.Button(frame,image=btn2,bd=0,highlightthickness = 0,command=queueType2)
button2.place(relx=0.29,rely=0.50)
button3 = tk.Button(frame,image=btn3,bd=0,highlightthickness = 0,command=queueType3)
button3.place(relx=0.29,rely=0.65)
button4 = tk.Button(frame,image=btn4,bd=0,highlightthickness = 0,command=queueType4)
button4.place(relx=0.29,rely=0.80)



root.mainloop()
