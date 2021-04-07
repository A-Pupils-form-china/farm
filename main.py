from tkinter import *
from tkinter import messagebox, Button
from pathlib import Path

from mune import mune


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.loginpane()

    def loginpane(self):

        self.label01 = Label(self, text="用户名", font=10).pack()

        self.entry01 = Entry(self, font=10)
        self.entry01.pack()
        self.label02 = Label(self, text="密码", font=10).pack()

        self.entry02 = Entry(self, font=10)
        self.entry02.pack()
        self.btn01 = Button(self, text="登录", command=self.signin).pack(side="left")
        self.btn02 = Button(self, text="注册", command=self.signup).pack(side="right")

    def signup(self):
        file = Path("D:\\user.txt")
        if file.is_file():
            messagebox.showinfo('警告', "已注册，请勿再次注册")
        else:
            self.forget()
            self.f1 = Frame(self.master)
            self.f1.pack()
            self.l1 = Label(self.f1, text="用户名", font=10)
            self.l1.pack()
            self.e1 = Entry(self.f1, font=10)
            self.e1.pack(side="top")
            self.l2 = Label(self.f1, text="密码", font=10)
            self.l2.pack(side="top")
            self.e2 = Entry(self.f1, font=10)
            self.e2.pack(side="top")
            self.l3 = Label(self.f1, text="再次输入密码", font=10)
            self.l3.pack(side="top")
            self.e3 = Entry(self.f1, font=10)
            self.e3.pack(side="top")
            self.b1 = Button(self.f1, text="注册", command=self.check)
            self.b1.pack()

    def check(self):
        if self.e2.get() == self.e3.get():
            messagebox.showinfo(title="完成", message="注册完成")
            f = open("D:\\user.txt", "w")
            f.write(self.e1.get() + " " + self.e2.get() + " 0")
            self.length = f.tell()
            f.close()
            self.f1.forget()
            self.pack()
        else:
            messagebox.showinfo(title="失败", message="请再注册一遍")

    def signin(self):
        username = self.entry01.get()
        password = self.entry02.get()
        print("用户名：" + self.entry01.get())
        print("密码： " + self.entry02.get())
        try:
            f = open('D:\\user.txt', "r+")
        except BaseException:
            messagebox.showinfo(message="未注册，请先注册")
        else:
            a = f.read().split(' ')
        if a[0] == username and a[1] == password:
            # messagebox.showinfo(self, message="登陆成功")
            self.destroy()
            mune(master=self.master)
        else:
            messagebox.showinfo(self, message="登陆失败")


root = Tk()
root.geometry("1600x900+100+100")
root.title("emm")
app = Application(master=root)
root = mainloop()
