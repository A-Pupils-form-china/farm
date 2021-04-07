import os
import sys
from os import remove
import time
from tkinter import Frame, Label, Entry, Text, Button, Tk, mainloop, messagebox


class mune(Frame):
    def __init__(self, master=None, ):
        self.vagetable = ({'uid': 0, 'name': '苹果', 'mature_time': 1, 'seed_price': 20, 'fruit_price': 50,
                           'experience': 10},
                          {'uid': 1, 'name': '香蕉', 'mature_time': 1, 'seed_price': 30, 'fruit_price': 70,
                           'experience': 20})

        super().__init__(master=None)
        self.time = time.localtime(time.time())
        self.master = master
        self.pack()
        self.frame1 = Frame(master).pack()
        self.initpane()

    def initpane(self):
        self.text = Text(self, width=100, height=20, font=('宋体', 20))
        self.text1 = Text(self.frame1, width=50, height=7, font=("宋体", 20))
        f1 = open("D:\\user.txt", "r")
        a = f1.readline().split(' ')
        temp = f1.readline().split(' ')
        self.seed_amount = {}
        for i in range(len(temp) - 1):
            self.seed_amount[i] = int(temp[i])
        temp = f1.readline().split(' ')
        self.fruit_amount = {}
        for i in range(len(temp) - 1):
            self.fruit_amount[i] = int(temp[i])
        temp = f1.readline().split(' ')
        self.sign = {}

        self.user = {'name': a[0], 'password': a[1], 'state': a[2]}
        if self.user['state'] == '0':
            self.text.insert(0.0, "欢迎" + a[0] + "来到这里,获得1000金币作为新手奖励以及一颗苹果种子\n按确定以继续")
            self.text['state'] = 'disabled'
            self.text.pack()
            self.user['state'] = 1
            self.user['money'] = 1000
            self.user['level'] = 0
            self.user['experience'] = 0
            self.user['field'] = 5
            self.seed_amount[0] = 1
            self.seed_amount[1] = 0
            self.fruit_amount[0] = 0
            self.fruit_amount[1] = 0
            self.sign['month'] = self.time.tm_mon
            self.sign['day'] = self.time.tm_mday
            f1.close()
            f1 = open("D:\\user.txt", "w+")
            b = list(self.user.values())
            for i in range(len(self.user)):
                f1.write(str(b[i]) + " ")
            f1.write("\n")
            f1.write(str(self.seed_amount[0]) + ' ' + str(self.seed_amount[1]) + ' \n')
            f1.write(str(self.fruit_amount[0]) + ' ' + str(self.fruit_amount[1]) + ' \n')
            f1.write(str(self.sign['month']) + ' ' + str(self.sign['day']) + ' \n')
            f2 = open("D:\\data.txt", "w+")
            for i in range(0, 6):
                f2.write('0 0 0 0 0 \n')
            self.btn01 = Button(self, text="确定", width=4, height=2, font=('宋体', 15), command=lambda: self.clean())
            self.btn01.pack(side="bottom", padx=20)
        else:
            self.user['money'] = int(a[3])
            self.user['level'] = int(a[4])
            self.user['experience'] = int(a[5])
            self.user['field'] = int(a[6])
            self.sign['month'] = int(temp[0])
            self.sign['day'] = int(temp[1])
            self.munepane()

    def clean(self):
        self.text['state'] = "normal"
        self.text.delete(0.0, "end")
        self.btn01.destroy()
        self.munepane()

    def munepane(self):
        f1 = open("D:\\data.txt", 'r+')
        self.data = {}
        temp = f1.readline().split(' ')
        self.data['mode'] = {}
        self.data['vaget'] = {}
        self.data['month'] = {}
        self.data['day'] = {}
        self.data['hour'] = {}
        self.data['min'] = {}

        for i in range(0, len(temp) - 1):
            self.data['mode'][i] = int(temp[i])
        temp = f1.readline().split(' ')
        for i in range(0, len(temp) - 1):
            self.data['vaget'][i] = int(temp[i])
        temp = f1.readline().split(' ')
        for i in range(0, len(temp) - 1):
            self.data['month'][i] = int(temp[i])
        temp = f1.readline().split(' ')
        for i in range(0, len(temp) - 1):
            self.data['day'][i] = int(temp[i])
        temp = f1.readline().split(' ')
        for i in range(0, len(temp) - 1):
            self.data['hour'][i] = int(temp[i])
        temp = f1.readline().split(' ')
        for i in range(0, len(temp) - 1):
            self.data['min'][i] = int(temp[i])
        f1.close()
        '''
        print(self.mode)
        print(self.vaget)
        print(self.month)
        print(self.day)
        print(self.hour)
        print(self.min)
        '''

        self.refresh()
        self.btn01 = Button(self.frame1, text='种植', width=10, height=5, command=lambda: self.plantpane1()).pack(
            side='right', padx=10)
        self.btn02 = Button(self.frame1, text='收获', width=10, height=5, command=lambda: self.reap()).pack(side='right',
                                                                                                          padx=10)
        self.btn03 = Button(self.frame1, text='商店', width=10, height=5, command=lambda: self.shoppane()).pack(
            side='right', padx=10)
        self.btn04 = Button(self.frame1, text='刷新', width=10, height=5, command=lambda: self.refresh()).pack(
            side='right', padx=10)
        self.btn05 = Button(self.frame1, text='卖出果实', width=10, height=5, command=lambda: sell()).pack(
            side='right', padx=10)
        self.btn06 = Button(self.frame1, text='退出', width=10, height=5, command=lambda: self.saving()).pack(
            side='right', padx=10)


        def sell():
            sum = self.fruit_amount[0] * self.vagetable[0]['fruit_price'] + self.fruit_amount[1] * self.vagetable[1][
                'fruit_price']
            if sum == 0:
                messagebox.showinfo('警告', '醒醒，你没东西可以卖')
            else:
                self.fruit_amount[0] = 0
                self.fruit_amount[1] = 0
                self.user['money'] += sum
                messagebox.showinfo('成功', '已卖出全部果实，获得' + str(sum) + '个金币')
            self.refresh()

        if self.sign['month'] != self.time.tm_mon or self.sign['day'] != self.time.tm_mday:
            messagebox.showinfo('签到', '签到成功，奖励100金币以及10经验')
            self.user['money'] += 100
            self.user['experience'] += 10
            self.sign['month'] = self.time.tm_mon
            self.sign['day'] = self.time.tm_mday

    def plantpane1(self):
        amount = 0
        for i in range(0, 2):
            if self.seed_amount[i] != 0:
                break
            else:
                amount += 1
        if amount == 2:
            messagebox.showinfo('警告', '没有种子了，请购买')

        else:
            self.root = Tk()
            self.root.title("请选择要种植的农作物")
            self.show = Frame(master=self.root)
            Button(self.root,
                   text=self.vagetable[0]['name'] + str(self.seed_amount[0]) if self.seed_amount[0] != 0 else '空',
                   width=10, height=2,
                   command=lambda: self.plantpane2(0, master=self.root)).pack(side="top")
            Button(self.root,
                   text=self.vagetable[1]['name'] + str(self.seed_amount[1]) if self.seed_amount[1] != 0 else '空',
                   width=10, height=2,
                   command=lambda: self.plantpane2(1, master=self.root)).pack(side="top")
            root = mainloop()

    def plantpane2(self, i1, master=None):
        self.f2 = Frame(master)
        self.show.destroy()
        Label(master, text='请选择种植的田地', font=20).pack()
        Button(master, text='1' if self.data['mode'][0] == 0 else "无法种植", width=10, height=5,
               command=lambda: self.plant(i1, 0) if self.data['mode'][0] == 0 else self.empty()).pack(side='top')
        Button(master, text='2' if self.data['mode'][1] == 0 else "无法种植", width=10, height=5,
               command=lambda: self.plant(i1, 1) if self.data['mode'][1] == 0 else self.empty()).pack(side='top')
        Button(master, text='3' if self.data['mode'][2] == 0 else "无法种植", width=10, height=5,
               command=lambda: self.plant(i1, 2) if self.data['mode'][2] == 0 else self.empty()).pack(side='top')
        Button(master, text='4' if self.data['mode'][3] == 0 else "无法种植", width=10, height=5,
               command=lambda: self.plant(i1, 3) if self.data['mode'][3] == 0 else self.empty()).pack(side='top')
        Button(master, text='5' if self.data['mode'][4] == 0 else "无法种植", width=10, height=5,
               command=lambda: self.plant(i1, 4) if self.data['mode'][4] == 0 else self.empty()).pack(side='top')

    def empty(self):
        pass

    def plant(self, i1, i=0):
        self.data['mode'][i] = 1
        self.data['vaget'][i] = self.vagetable[i1]['uid']
        self.seed_amount[i1] = self.seed_amount[i1] - 1
        self.data['month'][i] = self.localtime.tm_mon
        self.data['day'][i] = self.localtime.tm_mday
        self.data['hour'][i] = self.localtime.tm_hour + self.vagetable[i1]['mature_time']
        self.data['min'][i] = self.localtime.tm_min
        if self.data['hour'][i] >= 24:
            self.data['day'][i] += 1
            self.data['hour'][i] -= 24
        if self.data['day'][i] >= 30:
            self.data['month'] += 1
            self.data['day'] -= 30
        self.root.destroy()
        self.refresh()

    def count_time(self, b):
        for i in range(0, int(self.user['field'])):
            self.localtime = time.localtime(time.time())
            a = (self.data['month'][i] - self.localtime.tm_mon) * 43776 + (
                    self.data['day'][i] - self.localtime.tm_mday) * 1440 + (
                        self.data['hour'][i] - self.localtime.tm_hour) * 60 + (
                        self.data['min'][i] - self.localtime.tm_min)
            if a <= 0 and self.data['mode'][i] == 1:
                self.data['mode'][i] = 2
        if self.data['mode'][b] == 2:
            return 0
        else:
            return (self.data['month'][b] - self.localtime.tm_mon) * 43776 + (
                    self.data['day'][b] - self.localtime.tm_mday) * 1440 + (
                           self.data['hour'][b] - self.localtime.tm_hour) * 60 + (
                           self.data['min'][b] - self.localtime.tm_min)

    def shoppane(self):
        if int(self.user['money']) < 10:
            messagebox.showinfo('警告', '金币不足10，无法购买')
        else:
            self.root = Tk()
            self.root.title("请选择要购买的物品")
            global amount
            amount = [0, 0]
            self.show = Frame(master=self.root)

            apple = Button(master=self.show, text="苹果", font=20, command=lambda: temp(0))
            banana = Button(master=self.show, text="香蕉", font=20, command=lambda: temp(1))
            apple_amount = Label(master=self.show, text=str(amount[0]), font=20)
            banana_amount = Label(master=self.show, text=str(amount[1]), font=20)

            def temp(temp1):
                global i
                i = temp1

            apple.pack()
            apple_amount.pack()
            banana.pack()
            banana_amount.pack()
            self.show.pack()
            self.operate = Frame(master=self.root)
            btn01 = Button(master=self.root, text='+', width=5, height=3, font=20, command=lambda: add()).pack(
                side='left')

            btn02 = Button(master=self.root, text='-', width=5, height=3, font=20, command=lambda: add()).pack(
                side='right')
            btn03 = Button(master=self.root, text='确定', width=5, height=3, font=20, command=lambda: buy()
                           ).pack()

            def add():
                amount[i] += 1
                apple_amount['text'] = str(amount[0])
                banana_amount['text'] = str(amount[1])

            def buy():

                price = amount[0] * self.vagetable[0]['seed_price'] + amount[1] * self.vagetable[1]['seed_price']

                if int(self.user['money']) > price:
                    self.user['money'] = self.user['money'] - price
                    self.seed_amount[0] += amount[0]
                    self.seed_amount[1] += amount[1]
                    self.root.destroy()
                    self.refresh()
                else:
                    messagebox.showinfo('警告', '金币不足')

            self.operate.pack()

    def refresh(self):
        b = 1.0
        self.text1['state'] = 'normal'
        self.text1.delete(0.0, "end")

        self.text1.insert(0.0, "种子数量：苹果：" + str(self.seed_amount[0]) + ' 香蕉:' + str(self.seed_amount[1]) + "\n")
        self.text1.insert(0.0, "果实数量：苹果：" + str(self.fruit_amount[0]) + ' 香蕉:' + str(self.fruit_amount[1]) + '\n')
        self.text1.insert(0.0, "用户经验" + str(self.user['experience']) + '\n')
        self.text1.insert(0.0,
                          "姓名:" + self.user['name'] + "    用户金币: " + str(self.user['money']) + "    用户等级: " + str(
                              self.user[
                                  'level']) + "\n")
        self.count_time(0)
        self.text1['state'] = 'disable'
        self.text1.pack(side='left')
        self.text['state'] = 'normal'
        self.text.delete(0.0, "end")
        self.text.insert(0.0, "田               状态               种植植物               剩余成熟时间\n")
        for i in range(0, int(self.user['field'])):
            if self.data['mode'][i] == 0:
                self.text.insert(b + int(self.user['field']), str(i + 1) + "                 空\n")
            elif self.data['mode'][i] == 1:
                self.text.insert(b + int(self.user['field']),
                                 str(i + 1) + "                已种植              " + str(
                                     self.vagetable[int(self.data['vaget'][i])][
                                         'name']) + "                     " + str(
                                     self.count_time(i)) +
                                 '分钟\n')
            elif self.data['mode'][i] == 2:
                self.text.insert(b + int(self.user['field']),
                                 str(i + 1) + "                已成熟              " + str(
                                     self.vagetable[int(self.data['vaget'][i])]['name']) + "\n")
            b += 1
        self.text['state'] = "disable"
        self.text.pack()

    def reap(self):
        amount = 0
        get_experience = 0
        for i in range(0, int(self.user['field'])):
            if self.data['mode'][i] == 2:
                self.fruit_amount[self.data['vaget'][i]] += 1
                self.data['mode'][i] = 0
                amount += 1
                get_experience += self.vagetable[self.data['vaget'][i]]['experience']
        if amount != 0:
            messagebox.showinfo('收获', '已收获' + str(amount) + "颗果实,获得经验" + str(get_experience))
            self.user['experience'] += get_experience
        self.refresh()

    def saving(self):
        f1 = open('D:\\data.txt', 'w+')
        for i in range(0, 5):
            f1.write(str(self.data['mode'][i]) + ' ')
        f1.write('\n')
        temp1 = True
        for i in self.data.values():
            if temp1:
                temp1 = False
                continue
            temp = 0
            for a in i.values():
                if self.data['mode'][temp] == 1:
                    f1.write(str(a) + ' ')
                else:
                    f1.write('0 ')
                temp += 1
            f1.write('\n')
        '''
        for i in range(0, 5):
            f1.write(str(self.data['mode'][i]) + ' ')
            print(str(self.data['mode'][i]))
        f1.write('\n')
        for i in range(0, 5):
            if self.data['mode'][i] == 1:
                f1.write(str(self.data['vaget'][i]) + ' ')
            else:
                f1.write('0 ')
        f1.write('\n')
        for i in range(0, 5):
            if self.data['mode'][i] == 1:
                f1.write(str(self.data['month'][i]) + ' ')
            else:
                f1.write('0 ')
        f1.write('\n')
        for i in range(0, 5):
            if self.data['mode'][i] == 1:
                f1.write(str(self.data['day'][i]) + ' ')
            else:
                f1.write('0 ')
        f1.write('\n')
        for i in range(0, 5):
            if self.data['mode'][i] == 1:
                f1.write(str(self.data['hour'][i]) + ' ')
            else:
                f1.write('0 ')
        f1.write('\n')
        for i in range(0, 5):
            if self.data['mode'][i] == 1:
                f1.write(str(self.data['min'][i]) + ' ')
            else:
                f1.write('0 ')
        f1.write('\n')
        '''
        f2 = open("D:\\user.txt", 'w+')
        f2.write(str(self.user['name']) + " " + str(self.user['password']) + " " + str(self.user['state']) + " " + str(
            self.user[
                'money']) + " " + str(self.user['level']) + ' ' + str(self.user['experience']) + " " + str(
            self.user['field']) + ' \n')
        for i in range(0, 2):
            f2.write(str(self.seed_amount[i]) + ' ')
        f2.write('\n')
        for i in range(0, 2):
            f2.write(str(self.fruit_amount[i]) + ' ')
        f2.write('\n')
        for i in self.sign.values():
            f2.write(str(i) + ' ')
        sys.exit()
