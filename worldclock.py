from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()
root.geometry("500x250")
root.title("WorldClock")


def times():
    home = pytz.timezone("Asia/istanbul")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="Istanbul")

    home = pytz.timezone("Australia/Victoria")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="Australia")

    home = pytz.timezone("Africa/Timbuktu")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="Africa")

    home = pytz.timezone("America/New_York")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock4.config(text=current_time)
    name4.config(text="America")
    clock1.after(200, times)


name1 = Label(root, font="times 25 bold")

clock1 = Label(root, font="times 25 bold")

note1 = Label(root, text="Hours  Minutes  Seconds", font="times 10 bold")

name1.place(x=60, y=5)
clock1.place(x=50, y=40)
note1.place(x=50, y=80)

name2 = Label(root, font="times 25 bold")

clock2 = Label(root, font="times 25 bold")

note2 = Label(root, text="Hours  Minutes  Seconds", font="times 10 bold")

name2.place(x=50, y=120)
clock2.place(x=50, y=160)
note2.place(x=50, y=200)

name3 = Label(root, font="times 25 bold")

clock3 = Label(root, font="times 25 bold")

note3 = Label(root, text="Hours  Minutes  Seconds", font="times 10 bold")

name3.place(x=330, y=5)
clock3.place(x=310, y=40)
note3.place(x=310, y=80)

name4 = Label(root, font="times 25 bold")

clock4 = Label(root, font="times 25 bold")

note4 = Label(root, text="Hours  Minutes  Seconds", font="times 10 bold")

name4.place(x=315, y=120)
clock4.place(x=310, y=160)
note4.place(x=310, y=200)

times()
root.mainloop()
