import sys
import tkinter as tk
import os
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog, Text
from PIL import Image,ImageTk
from tkinter import messagebox

ris = Tk()
top = Toplevel() #Creates the toplevel window
top.title("RIS v2.0 Login")
top.geometry('370x500')
top.configure(bg='#333333')
top.iconbitmap('C:\PROJECT\RIS\kontron.ico')
top.resizable(0,0)

login_label = Label(top, text="RIS Login", bg='#333333',fg="#FFFFFF", font=("Arial", 30, 'bold'))
username_label = Label(top, text="Username: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = Entry(top, font=('Arial',16)) #Username entry
password_entry = Entry(top, show='*', font=('Arial',16)) #Password entry
password_label = Label(top, text="Password: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
button1 = Button(top, text="Login", command=lambda:command1(), bg="#222d82", fg="#FFFFFF", font=("Arial",15,)) #Login button
button2 = Button(top, text="Exit", command=lambda:command2(), bg="#c20414", fg="#FFFFFF", font=("Arial", 15))  #Cancel button


login_label.grid(row=0, column=8, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=8)
username_entry.grid(row=1, column=9, pady=10)
password_entry.grid(row=2, column=9, pady=10)
password_label.grid(row=2, column=8)
button1.grid(row=3, column=8, columnspan=2, pady=30)
button2.grid(row=4,column=8,columnspan=2, pady=15)


def command1():
    if username_entry.get() == "adminhw" and password_entry.get() == "kontronhw": #Checks whether username and password are correct
        messagebox.showinfo(title="Well Done", message="Login Successful. Welcome to RIS.")
        ris.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
    else:
        messagebox.showerror(title="Error Login", message="Invalid. Please try again.")

def command2():
    top.destroy() #Removes the toplevel window
    ris.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


ris.title('RIS v2.0')
ris.iconbitmap('C:\PROJECT\RIS\kontron.ico')
ris.geometry("950x500")


bg= PhotoImage(file="C:\PROJECT\RIS\RIS20.png")

my_label = Label(ris, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

    
def Call_Borrow():
    os.system('python RIS\Borrow.py')

def Call_Return():
    os.system('python RIS\Return.py')

def Call_Report():
    os.system('python RIS\Report.py')

def Call_Clear_Report():
    os.system('python RIS\Clear_Report.py')

mybutton  = Button(ris,bg="#222d82",fg= 'white',  text = 'BORROW ITEM', height=5, width=25, font = ('Arial', 12, 'bold'), command= Call_Borrow)
mybutton2 = Button(ris,bg="#222d82",fg= 'white', text = 'RETURN ITEM', height=5, width=25, font = ('Arial', 12, 'bold'), command= Call_Return)
mybutton3 = Button(ris,bg="#222d82",fg= 'white', text = 'REPORT', height=5, width=25, font = ('Arial', 12, 'bold'), command= Call_Report)
mybutton4 = Button(ris,bg="#222d82",fg= 'white', text = 'CLEAR REPORT', height=5, width=25, font = ('Arial', 12, 'bold'), command= Call_Clear_Report)
mybutton5 = Button(ris,bg="#c20414",fg= 'white', text = 'EXIT', height=2, width=20,  command = ris.quit, font = ('Arial', 12, 'bold'))
mylabel6 = Label(ris,bg="#00010a",fg= 'white', text = 'Remote Inventory System', height=2, width=20, font = ('Arial', 18, 'bold'))

mybutton.grid(row=0, column=0, sticky = 'news')

mybutton.pack()
mybutton2.pack()
mybutton3.pack()
mybutton4.pack()
mybutton5.pack()
mylabel6.pack()

mybutton.place(x=35, y=100, relx=0.1, rely=0.1)
mybutton2.place(x=35, y=220, relx=0.1, rely=0.1)
mybutton3.place(x=465, y=100, relx=0.1, rely=0.1)
mybutton4.place(x=465, y=220, relx=0.1, rely=0.1)
mybutton5.place(x =273, y=350, relx=0.1, rely=0.1)
mylabel6.place(x =225, y=0, relx=0.1, rely=0.1)


ris.resizable(0,0)

ris.withdraw()
ris.mainloop() 