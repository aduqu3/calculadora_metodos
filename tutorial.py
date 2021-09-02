import sys
sys.path.append("./")
from metodos.simpson_1_3 import *
# 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import BOTH
# 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text

# colocar iconos o imagenes en ventanas
# from PIL import ImageTk,ImageTk

# from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor

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
def graph(f, n, a, b):
    # t = np.arange(0, 3, .01)
    # ln(x) + sin(3x) + e^4
    # plt.plot(t, 2 * np.sin(2 * np.pi * t))
    # x = np.linspace(0, 3, .01)
    
    x = np.linspace(a, b, n)
    func = string2func(f)
    plt.plot(x, func(x))
    plt.xlim(a, b)
    plt.show()


#===============metodo de simpson 1/3=========================================INICIO
def window_simpson_13():
    global window_1
   

    def press(func_d, n_d, a_d, b_d):
        # print(str.get())
        func = func_d.get()
        n = n_d.get()
        a = a_d.get()
        b = b_d.get()

        print(func)
        print(n)
        print(a)
        print(b)
        print("imprimir len")
        print(len(func))
        print(len(n))
        print(len(a))
        print(len(b))
        
        if( len(func) and len(n) and len(a) and len(b) ):
            print("vamos a hacer algo")
            n = int(n)
            a = int(a)
            b = int(b)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_1, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # llamar metodo simpson 1/3
            # luego mostrarlo en la venta
            # n = 100
            # a = 0.0
            # b = 1.0
            # f = 'x**2+2*x-3'
            # print(simpson13(n, a, b, f))

            var = tk.IntVar()
            btn_clean = ttk.Button(window_1, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables
            btn_graph.destroy()
            # btn_clean.destroy()
            # window_1.destroy()
            func = ''
            n = ''
            a = ''
            b = ''
            func_d.set('')
            n_d.set('')
            a_d.set('')
            b_d.set('')
        else:
            print("vacio")
            

    window_1 = tk.Toplevel(root)
    window_1.geometry("800x400")
    window_1.title("Simpson 1/31")
    # window_1.resizable(False, False)
    lbl = tk.Label(window_1, text="El metodo de simpson 1/3...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_1, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_1, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # n
    n_lbl = ttk.Label(window_1, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_1, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 

    # a
    a_lbl = ttk.Label(window_1, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_1, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_1, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_1, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 
    

    
    submit_btn = ttk.Button(window_1, text = "calcular", command=lambda: press(func_str, n_str, a_str, b_str)).pack()

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

#
# assets of main window
#

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
