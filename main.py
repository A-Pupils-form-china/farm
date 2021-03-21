from tkinter import *
from tkinter import messagebox, Button


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        v1 = StringVar()
        v1.set("abc")
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()

        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        v2.set("123")
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.setvar("123")
        self.entry02.pack()

        self.btn01 = Button(self, text="LOGIN", command=self.login)
        self.btn01.pack()

    def login(self, ):

        username=self.entry01.get()
        password=self.entry02.get()
        print("用户名：" + self.entry01.get())
        print("密码： " + self.entry02.get())
        f = open('test.txt', "r")
        a = f.read().split('\n')
        if a[0] == username and a[1] == password :
            messagebox.showinfo(self, message="登陆成功")
        else:
            messagebox.showinfo(self, message="登陆失败")


root = Tk()
root.geometry("800x800+200+300")
root.title("emm")
app = Application(master=root)
root = mainloop()
