from tkinter import *
from tkinter import messagebox, Button


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
       self.l=Label(self, width=10, height=5)
       self.l["text"]="emmm"
       self.l.pack()

    def emmm(self):
        messagebox.showinfo("emm", "woshiyigechuangkou")


root = Tk()
root.geometry("800x800+200+300")
root.title("emm")
app = Application(master=root)
root = mainloop()
