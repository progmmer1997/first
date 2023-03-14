
from tkinter import *


root = Tk()
root.geometry('700x300')

w1 = Entry(width=15)
w1.place(x = 10, y = 100)

w2 = Entry(width=15)
w2.place(x = 120, y = 100)

w3 = Entry(width=15)
w3.place(x = 230, y = 100)

w4 = Entry(width=15)
w4.place(x = 340, y = 100)

n = 0
w1.focus()

def Inc1(*args):
    global n
    n += 1
    root.title(n)
    if n == 10:
        w2.focus()

def Dec1(*args):
    global n
    if n > 0:
        n -= 1
    root.title(n)        

def Inc2(*args):
    global n
    n += 1
    root.title(n)
    if n == 20:
        w3.focus()

def Dec2(*args):
    global n
    n -= 1
    root.title(n)
    if n == 10:
        w1.focus()        

def Inc3(*args):
    global n
    n += 1
    root.title(n)
    if n == 30:
        w4.focus()

def Dec3(*args):
    global n
    n -= 1
    root.title(n)
    if n == 20:
        w2.focus()        

def Inc4(*args):
    global n
    if n < 40:
        n += 1
    root.title(n)
    if n == 40:
        w4["state"] = DISABLED

def Dec4(*args):
    global n
    if n == 40:
        w4["state"] = NORMAL
    n -= 1
    root.title(n)
    if n == 30:
        w3.focus()        


w1.bind("<Key>", Inc1)

w1.bind("<BackSpace>", Dec1)

w2.bind("<Key>", Inc2)

w2.bind("<BackSpace>", Dec2)

w3.bind("<Key>", Inc3)

w3.bind("<BackSpace>", Dec3)

w4.bind("<Key>", Inc4)

w4.bind("<BackSpace>", Dec4)


def c4(*args):
    global n
    if n==39:

        w4.delete(0,END)
        n=n-8
        root.title(n)
        w3.focus()
        w3.delete(0, END)
        n=n-10
        root.title(n)
        w2.focus()
        w2.delete(0, END)
        n=n-11
        root.title(n)
        w1.focus()
        w1.delete(0, END)
        n=n-10
        root.title(n)
        w1.focus()


b=Button(root,text='clear',command=c4).pack(pady=130)

root.mainloop()






