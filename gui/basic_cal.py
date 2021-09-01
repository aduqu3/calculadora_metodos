import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar,Entry,Button
from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor

win = tk.Tk()

win.title("Calculadora")

# win.geometry('300x300+500+200')

# label = tk.Label(win,text="Hola mundo")
# button =  ttk.Button(win,text="Hola")

# label.pack()
# button.pack()

expr = ''

# cada vez que presione los captura...
text = tk.StringVar()

def press(num):
    global expr
    expr += str(num)
    text.set(expr)

def clear():
    global expr
    expr = ''
    text.set(expr)

def equal():
    global expr
    # print(len(expr))
    if(len(expr) == 0):
        print("error: no ingreso ningun elemento")
    else:
        ttl = str(eval(expr))
        text.set(ttl)

def clear():
    global expr
    expr = ''
    text.set(expr)

# entry
entry = ttk.Entry(win, justify='right', textvariable=text)
entry.grid(row=0, columnspan=5, sticky='nsew')
entry.focus()

# row 1
btn_7 = ttk.Button(win, text='7', command=lambda:press('7'))
btn_7.grid(row=1, column=0)

btn_8 = ttk.Button(win, text='8', command=lambda:press(8))
btn_8.grid(row=1, column=2)

btn_9 = ttk.Button(win, text='9', command=lambda:press(9))
btn_9.grid(row=1, column=3)

btn_d = ttk.Button(win, text='/', command=lambda:press('/'))
btn_d.grid(row=1, column=4)

# row 2
btn_4 = ttk.Button(win, text='4', command=lambda:press(4))
btn_4.grid(row=2, column=0)

btn_5 = ttk.Button(win, text='5', command=lambda:press(5))
btn_5.grid(row=2, column=2)

btn_6 = ttk.Button(win, text='6', command=lambda:press(6))
btn_6.grid(row=2, column=3)

btn_m = ttk.Button(win, text='*', command=lambda:press('*'))
btn_m.grid(row=2, column=4)

# row 3
btn_1 = ttk.Button(win, text='1', command=lambda:press(1))
btn_1.grid(row=3, column=0)

btn_2 = ttk.Button(win, text='2', command=lambda:press(2))
btn_2.grid(row=3, column=2)

btn_3 = ttk.Button(win, text='3', command=lambda:press(3))
btn_3.grid(row=3, column=3)

btn_s = ttk.Button(win, text='-', command=lambda:press('-'))
btn_s.grid(row=3, column=4)

# row 4
btn_0 = ttk.Button(win, text='0', command=lambda:press(0))
btn_0.grid(row=4, column=0)

btn_dot = ttk.Button(win, text='.', command=lambda:press('.'))
btn_dot.grid(row=4, column=2)

btn_c = ttk.Button(win, text='C', command=clear)
btn_c.grid(row=4, column=3)

btn_a = ttk.Button(win, text='+', command=lambda:press('+'))
btn_a.grid(row=4, column=4)

# row 5
btn_e = ttk.Button(win, text='=', command=equal)
btn_e.grid(row=5, columnspan=5, sticky='nsew')

# 
win.mainloop()
 