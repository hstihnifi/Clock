from tkinter import *

global count


class Stopwatch:

    def __init__(self):
        self.root = Tk()
        self.root.title("Stop Watch")
        self.root.geometry("550x200")

        self.t = StringVar()
        self.t.set("00:00:00")
        self.lap_string = StringVar()
        self.lap_string.set("00:00:00")

        self.lap_lb = Label(self.root,
                            textvariable=self.lap_string,
                            font="Times 25 bold",
                            bg="black",
                            fg="aquamarine4")

        self.lb = Label(self.root,
                        textvariable=self.t,
                        font="Times 40 bold",
                        bg="black",
                        fg="SeaGreen1")

        self.bt1 = Button(self.root,
                          text="Start ",
                          command=self.start,
                          font="Times 12 bold",
                          bg="black",
                          fg="PaleGreen1")

        self.bt2 = Button(self.root,
                          text=" Lap ",
                          command=self.lap,
                          font="Times 12 bold",
                          bg="black",
                          fg="PaleGreen1")

        self.bt3 = Button(self.root,
                          text="Reset",
                          command=self.reset,
                          font="Times 12 bold",
                          bg="black",
                          fg="PaleGreen1")

        self.bt4 = Button(self.root,
                          text=" Stop ",
                          command=self.stop,
                          font="Times 12 bold",
                          bg="black",
                          fg="PaleGreen1")

        self.bt5 = Button(self.root,
                          text=" Exit ",
                          command=self.close,
                          font="Times 12 bold",
                          bg="black",
                          fg="PaleGreen1")
        self.label = Label(self.root,
                           text="",
                           font="Times 40 bold")

        self.lb.place(x=171, y=-6)
        self.lap_lb.place(x=209, y=50)
        self.bt1.place(x=50, y=120)
        self.bt2.place(x=150, y=120)
        self.bt3.place(x=250, y=120)
        self.bt4.place(x=350, y=120)
        self.bt5.place(x=450, y=120)

        self.d = None
        self.root.configure(bg='black')
        self.root.mainloop()

    def reset(self):
        global count
        count = 1
        self.t.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.timer()

    def stop(self):
        global count
        count = 1

    def close(self):
        self.root.destroy()

    def timer(self):
        global count
        if count == 0:
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.t.set(self.d)
            if count == 0:
                self.root.after(1000, self.timer)

    def lap(self):
        self.lap_string.set(self.t.get())


a = Stopwatch()
