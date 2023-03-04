import time
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x200")

root.configure(bg="black")

root.title("Timer")

Label(root,
      text="'Countdown'",
      font="Helvetica 23 bold",
      bg="black",
      fg="RoyalBlue1").pack(pady=9)

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root,
                  width=3,
                  font=("Times 40 bold", 25, ""),
                  bg="black",
                  fg="SteelBlue",
                  textvariable=hour)

hourEntry.place(x=60, y=60)

minuteEntry = Entry(root,
                    width=3,
                    font=("Times 40 bold", 25, ""),
                    bg="black",
                    fg="SteelBlue",
                    textvariable=minute)

minuteEntry.place(x=120, y=60)

secondEntry = Entry(root,
                    width=3,
                    font=("Times 40 bold", 25, ""),
                    bg="black",
                    fg="SteelBlue",
                    textvariable=second)

secondEntry.place(x=180, y=60)


def submit():
    global temp
    try:

        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up ")

        temp -= 1


def exit():
    root.destroy()


btn1 = Button(root,
              text='Set Time',
              bd='10',
              bg="cyan4",
              fg="black",
              command=submit)

btn2 = Button(root,
              text=" Exit ",
              bg="black",
              fg="cyan4",
              command=exit)

btn1.place(x=114, y=120)
btn2.place(x=250, y=160)

root.mainloop()
