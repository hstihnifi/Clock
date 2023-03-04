from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.geometry("500x130")
root.title('Digital Clock')
root.configure(bg="gray25")


def time():
    string = strftime('%H:%M:%S %p')
    lb.config(text=string)
    lb.after(1000, time)


lb = Label(root,
           font='calibri 60 bold',
           background='gray25',
           foreground='white')

lb.pack(anchor='center')
time()

mainloop()
