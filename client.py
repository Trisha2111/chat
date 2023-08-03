import socket
from threading import Thread
from tkinter import *


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
port=8000
client.connect((ip,port))
print("Connected with the server")

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.header=Label(self.login,text="PLEASE LOGIN TO CONTINUE!",justify=CENTER,font="Helvetica 14 bold")
        self.header.place(relheight=0.15,relx=0.15,rely=0.07)

        self.labelname=Label(self.login,text="NAME: ",font="Helvetica 14 ")
        self.labelname.place(relheight=0.2,relx=0.1,rely=0.2)

        self.name=Entry(self.login,font="Helvetica 14")
        self.name.place(relwidth=0.4,relheight=0.15,relx=0.4,rely=0.2)
        self.name.focus()

        self.button=Button(self.login,text="LOGIN",font="Helvetica 14 bold",command=lambda: self.goahead(self.name.get()))
        self.button.place(relx=0.4,rely=0.55)


        self.Window.mainloop()
    
    def goahead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)
        rcv.start

    def recieve(self):
        while True:
            try:
                message=client.recv(2048).decode("utf-8")
                if message =="NICKNAME":
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except:
                print("An Error occured")
                client.close()
                break
        


g=GUI()