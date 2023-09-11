import socket
import time
import threading
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=4050
    maxconnection=99
    ip="LAPTOP-8HJI2EDD"
    print(ip)

    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address)=listensocket.accept()

    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(0)
            firstbox.insert(0, "Client : "+ sendermessage)

xr=0

def sendmsg():
    global xr
    if xr==0:
        s=socket.socket()
        hostname="LAPTOP-8HJI2EDD"
        port=3050
        s.connect((hostname,port))
        msg=messagebox.get()
        firstbox.insert(0, "You : "+ msg)
        s.send(msg.encode())
        xr=xr +1

    else:
        msg=messagebox.get()
        firstbox.insert(0, "You : "+ msg)
        s.send(msg.encode())


def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()


startpic= Image.open('start.png')
resized= startpic.resize((200, 90), Image.ANTIALIAS)

startchatimage=ImageTk.PhotoImage(resized)

buttons=Button(root,image=startchatimage, command=func, borderwidth=0)
buttons.place(x=50,y=5) 

message=StringVar()
messagebox=Entry(root,textvariable=message, font=('aerial', 10, 'bold'), border=2,width=32)
messagebox.place(x=10, y=445)
# messagebox.pack(pady=5)

sendpic= Image.open('send.png')
resized2= sendpic.resize((40, 40), Image.ANTIALIAS)

sendmessageimg=ImageTk.PhotoImage(resized2)

sendmessagebutton=Button(root,image=sendmessageimg, command=threadsendmsg, borderwidth=0)
sendmessagebutton.place(x=245,y=435)

firstbox=Listbox(root,height=20, width=43)
firstbox.place(x=15, y=110)
# firstbox.pack(pady=5)

root.mainloop()




