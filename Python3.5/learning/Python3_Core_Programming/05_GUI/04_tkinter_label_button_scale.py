from tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.geometry('250x150')
label = Label(top, text='hello world', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
button_quit = Button(top, text='quit', command=top.quit, activebackground='black', activeforeground='red')
button_quit.pack()
mainloop()