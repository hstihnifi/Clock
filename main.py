import os
from tkinter import *


class Menu:

    def __init__(self):
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("400x400")

        self.bt1 = Button(self.root,
                          text="  Alarm  ",
                          command=self.alarm,
                          font="Helvetica 14",
                          bg="Black",
                          fg="cornflower blue")

        self.bt2 = Button(self.root,
                          text="  Timer  ",
                          command=self.timer,
                          font="Helvetica 14",
                          bg="black",
                          fg="cornflower blue")

        self.bt3 = Button(self.root,
                          text="StopWatch ",
                          command=self.stopwatch,
                          font="Helvetica 14",
                          bg="Black",
                          fg="cornflower blue")

        self.bt4 = Button(self.root,
                          text="DigitalClock",
                          command=self.digital,
                          font="Helvetica 14",
                          bg="black",
                          fg="cornflower blue")

        self.bt5 = Button(self.root,
                          text=" World Clock ",
                          command=self.world_clock,
                          font="Helvetica 14",
                          bg="black",
                          fg="cornflower blue")

        self.bt6 = Button(self.root,
                          text=" Exit ",
                          command=self.exit,
                          font="Helvetica 10",
                          bg="black",
                          fg="cornflower blue")

        self.lb1 = Label(self.root,
                         text="'Waky Waky'",
                         font="Times 40 bold",
                         bg='DarkViolet',
                         fg='black')

        self.lb2 = Label(self.root,
                         text="Stay On Time With Us'",
                         font="Times 15 bold",
                         bg='DarkViolet',
                         fg='white')

        self.bt1.place(x=60, y=130)
        self.bt2.place(x=60, y=210)
        self.bt3.place(x=230, y=210)
        self.bt4.place(x=230, y=130)
        self.bt5.place(x=130, y=300)
        self.bt6.place(x=345, y=360)
        self.lb1.place(x=40, y=10)
        self.lb2.place(x=100, y=70)
        self.root.configure(bg='DarkViolet')
        self.root.mainloop()

    def alarm(self):
        os.system("python alarm.py")

    def stopwatch(self):
        os.system("python stopwatch.py")

    def timer(self):
        os.system("python timer.py")

    def digital(self):
        os.system("python digitalclock.py")

    def world_clock(self):
        os.system("python worldclock.py")

    def exit(self):
        self.root.destroy()


m = Menu()
