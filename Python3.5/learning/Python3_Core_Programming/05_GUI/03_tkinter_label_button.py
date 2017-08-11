from tkinter import *


top = Tk()

hello = Label(top, text='hello world!')
hello.pack()

button_quit = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
button_quit.pack(fill=X, expand=1)

mainloop()