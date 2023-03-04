from tkinter import *
import datetime
import time
from threading import *

from audioplayer import AudioPlayer

paused = False
player = None

root = Tk()

root.geometry("300x300")

root.title("Alarm")

root.configure(bg='black')


def threading():
    t1 = Thread(target=alarm_clock)
    t1.start()


def alarm_clock():
    global player
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)

        # get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(set_alarm_time)
        print(current_time)

        if current_time == set_alarm_time:
            fname = "SOAD.mp3"
            changevolume(0)
            player = AudioPlayer(fname)

            print("Waky Waky")
            try:
                player.play()
            except Exception as e:
                print(e)

            break


def dismiss():
    root.destroy()


def changevolume(delta):
    global player
    if not player is None:
        player.volume += delta


Label(root,
      text="'Set Your Alarm'",
      font="Helvetica 23 bold",
      bg="black",
      fg="dark violet").pack(pady=20)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08',
         '09', '10', '11', '12', '13', '14', '15', '16', '17',
         '18', '19', '20', '21', '22', '23', '24')

hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
    '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
    '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
    '52', '53', '54', '55', '56', '57', '58', '59', '60')

minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
    '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
    '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
    '52', '53', '54', '55', '56', '57', '58', '59', '60')

second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,
       text="Push To Set",
       font="Helvetica 15",
       bg="MediumPurple3",
       fg="black",
       command=threading).pack(pady=30)

Button(root,
       text="Dismiss",
       font="Helvetica 15",
       bg="black",
       fg="Magenta2",
       command=dismiss).pack(pady=15)

root.mainloop()
