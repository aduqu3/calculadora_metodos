import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import BOTH

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import text

from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor

# colocar iconos o imagenes en ventanas
# from PIL import ImageTk,ImageTk

root = tk.Tk()

# =======convierte un string a una funcion======================================
# there should be a better way using regex
replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    '^': '**',
    'pi': 'np.pi'
}

# think of more security hazards here
forbidden_words = [
    'import',
    'shutil',
    'sys',
    'subprocess',
]

def string2func(string):
    ''' evaluates the string and returns a function of x '''
    for word in forbidden_words:
        if word in string:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    # print(string)
    # return string

    def func(x):
        return eval(string)

    return func

# =============grafica una funcion dada========================================
def graph(str):
    # t = np.arange(0, 3, .01)
    # ln(x) + sin(3x) + e^4
    # plt.plot(t, 2 * np.sin(2 * np.pi * t))
    # x = np.linspace(0, 3, .01)

    func = string2func(str)
    x = np.linspace(0, 2, 250)
    plt.plot(x, func(x))
    plt.xlim(0, 2)
    plt.show()


#===============metodo de simpson 1/3=========================================INICIO
def window_simpson_13():
    global window_1
   

    def press(str):
        # print(str.get())
        expr = str.get()
        print(expr)
        if(expr == ''):
            print("esta vacio")
        else:
            print("no esta vacio")
            print(expr)

            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_1, text="Graficar", command=lambda: graph(expr))
            btn_graph.pack()

            var = tk.IntVar()
            btn_clean = ttk.Button(window_1, text="Limipiar", command=lambda: var.set(1))
            btn_clean.place(relx=.5, rely=.5, anchor="c")

            print("waiting...")
            btn_clean.wait_variable(var)
            print("done waiting.")

            # limpiar variables
            # btn_graph.destroy()
            # btn_clean.destroy()
            window_1.destroy()
            expr=''
            str.set('')

    window_1 = tk.Toplevel(root)
    window_1.geometry("800x250")
    window_1.title("Simpson 1/31")
    # window_1.resizable(False, False)
    lbl = tk.Label(window_1, text="El metodo de simpson 1/3...")
    lbl.pack(fill = BOTH)

    # colocar label para el input
    lbl_entry = ttk.Label(window_1, text = "Password")
    lbl_entry.pack()

    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    tk_string = tk.StringVar()
    entry = ttk.Entry(window_1, textvariable=tk_string)
    entry.configure(background="white")
    entry.focus()
    entry.pack()
    
    
    # entry=Entry(window,textvariable=self.string)
    #     entry.grid(row=0,column=0,columnspan=6)
    #     entry.configure(background="white")
    #     entry.focus()
    # .place(x = 110, y = 60)  
    submit_button = ttk.Button(window_1, text = "Submit", command=lambda: press(tk_string)).pack()
    # .place(x = 40, y = 130)
    # .place(x = 40,y = 100) 
    # btn close window
    # btn_close = tk.Button(window_1, text="Close window",command=lambda: window_1.destroy())
    # btn_close.pack()
#===============metodo de simpson  1/3 =========================================FIN



#===============ventana acerca de nosotros=========================================INICIO
def window_about_us():
    global window_aboutus
    window_aboutus = tk.Toplevel(root)
    window_aboutus.geometry("800x250")
    window_aboutus.title("Acerca de nosotros")
    # window_1.resizable(False, False)
    lbl = tk.Label(window_aboutus, text="Calculadora Metodos Numericos, este proyecto implementa diversos metodos observados en el trancurso de la material Metodos Numericos.\nProfesor: XXXXX \n Integrantes:\n Andres Duque 160003812\n Fredy Segura 1600038XX")
    lbl.pack(fill = BOTH, expand = 1)

    # # btn graficar ecuacion
    # btn_graph = ttk.Button(window_aboutus, text="Graficar", command=graph)
    # btn_graph.pack()
    # # btn2.grid(row=0, column=0)

    # # btn close window
    # btn_close =tk.Button(window_aboutus, text="Close window", command=lambda: window_aboutus.destroy())
    # btn_close.pack()
#===============ventana acerca de nosotros=========================================FIN

# assets of main window

# btn para ventana simpson 1/3
btn0 = tk.Button(root, text="Simpson 1/3", command=window_simpson_13)
btn0.pack(padx=20, pady=20)

# btn para ventana acerca de nosotros
btn_about_us = tk.Button(
    root, text="Acerca de nosotros", command=window_about_us)
btn_about_us.pack(padx=20, pady=20)

# btn1 = tk.Button(root, text="Simpson 1/3", command=openwindow)
# btn1.pack(padx=20, pady=20)

# size de la ventana
root.geometry("500x500")
# configuracion de la ventana principal
root.title("Calculadora Metodos Numericos")
# # root.iconbitmap('c:/gui/codemy.ico')
# root.geometry('400x200')
#
root.mainloop()
