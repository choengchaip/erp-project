import win32print, win32ui, win32con
import os,sys
import tkinter as tk
import datetime
import requests
import datetime
import time
from multiprocessing import Process
from PIL import Image, ImageWin

printer_name = win32print.GetDefaultPrinter()

def sendToPrinter(data):
    X=0; Y=10
    height = 1200
    multi_line_string = data.splitlines()  
    hDC = win32ui.CreateDC ()
    ### Set default printer from Windows
    :
    hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
    hDC.StartDoc ("dfs")
    hDC.StartPage ()
    hDC.TextOut(0,0,'******************************')
    Y += 50
    for line in multi_line_string:
        hDC.TextOut(X,Y,line)
        Y += 50
        height -= 50
    hDC.TextOut(0,height,'******************************')
    hDC.EndPage ()
    hDC.EndDoc ()

class ModelData:
    def __init_(self):
        self.weight = 0.0
    def calculateData(self):
        x = datetime.datetime.now()
        data = "วันที่ : "+str(x.strftime("%x"));
        data += "\nเวลา : "+str(x.strftime("%X"));
        data += "\nน้ำหนักที่ชั่งได้ : " + str(self.weight) + "กิโลกรัม"
        print(data)
        sendToPrinter(data)

    def sendRequest(self):
      query = {'type':'ฝากเงิน/ถอนเงิน'}
      r = requests.get(url='http://localhost:27580/', params=query,timeout=1)
      jsonData = r.json()
      label = tk.Label(frame,bg='white',text=str(jsonData['weight'])+" กิโลกรัม").place(height=40,relwidth=0.25,relx=0.375,rely=0.25)
      i = jsonData['weight']
      root.after(1000,self.sendRequest)
      self.weight = jsonData['weight']

model = ModelData()
i=str(0)
root = tk.Tk()
canvas = tk.Canvas(root,width = 1280,height=720)
canvas.pack()
frame = tk.Frame(root)
frame.place(relwidth=1,relheight=1)
button = tk.Button(frame, text="ยืนยัน",bg="grey", command=model.calculateData).place(height=40,relwidth=0.25,relx=0.375,rely=0.55)
label = tk.Label(frame,bg='white',text=i).place(height=40,relwidth=0.25,relx=0.375,rely=0.25)

root.after(1000, model.sendRequest)
root.mainloop()


    

    
