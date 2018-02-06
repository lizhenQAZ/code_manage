from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror
from functools import partial as pto

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS={
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU
}

critCB = lambda: showwarning('Error', 'Error Button Pressed')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed')
infoCB = lambda: showinfo('Info', 'Info Button Pressed')

top = Tk()
top.title('Road Signs')
Button(top, text='quit', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, fg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, fg='white')

for eachsign in SIGNS:
    signtype = SIGNS[eachsign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signtype.title(), eachsign, '.upper()' if signtype == CRIT else '.title()')
    eval(cmd)

top.mainloop()