import sys
# from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
sys.path.append("./")
from metodos.funciones import *
# 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import BOTH


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

# sin(2*pi*x)+x^2
# sin(2*np.pi*x)+x**2

def string2func(string):
    ''' evalua el string y retorna una funcion de x '''
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


#========================= WINDOW metodo de simpson 1/3 ========================================= INI
def window_simpson_13():
    global window_1
   

    def press(func_d, a_d, b_d, n_d,):
        # print(str.get())
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()

        # print(func)
        # print(n)
        # print(a)
        # print(b)
        # print("imprimir len")
        # print(len(func))
        # print(len(n))
        # print(len(a))
        # print(len(b))
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = int(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_1, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_1, text=('Resultado Simpson 1/3: ',simpson_13(a, b, n, func)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_1, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
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
            print("vacio: por favor ingrese todos los campos")
            

    window_1 = tk.Toplevel(root)
    window_1.geometry("800x400")
    window_1.title("Simpson 1/3")
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

    # n
    n_lbl = ttk.Label(window_1, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_1, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_1, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW metodo de simpson 1/3 ========================================= FIN


#========================= WINDOW METODO TRAPECIOS ========================================= INI
def window_trapecios():
    global window_2
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = int(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_2, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_2, text=('Resultado Trapecios: ', trapecios(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_2, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
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
            print("vacio: por favor ingrese todos los campos")
            

    window_2 = tk.Toplevel(root)
    window_2.geometry("800x400")
    window_2.title("Trapecios")
    
    lbl = tk.Label(window_2, text="El metodo de trapecios...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_2, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_2, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_2, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_2, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_2, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_2, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_2, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_2, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_2, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO TRAPECIOS ========================================= FIN

#========================= WINDOW METODO BISECCION ========================================= INI
def window_biseccion():
    global window_3
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = int(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_3, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_3, text=('Resultado Biseccion: ',bisection(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_3, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
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
            print("vacio: por favor ingrese todos los campos")
            

    window_3 = tk.Toplevel(root)
    window_3.geometry("800x400")
    window_3.title("Biseccion")
    
    lbl = tk.Label(window_3, text="El metodo de Biseccion...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_3, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_3, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_3, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_3, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_3, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_3, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_3, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_3, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_3, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO BISECCION ========================================= FIN

#========================= WINDOW METODO SIMPSON 3/8 ========================================= INI
def window_simpson_38():
    global window_4
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = int(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_4, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_4, text=('Resultado Simpson 3/8: ',simpson_38(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_4, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
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
            print("vacio: por favor ingrese todos los campos")
            

    window_4 = tk.Toplevel(root)
    window_4.geometry("800x400")
    window_4.title("Simpson 3/8")
    
    lbl = tk.Label(window_4, text="El metodo de Simpson 3/8...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_4, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_4, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_4, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_4, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_4, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_4, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_4, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_4, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_4, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO SIMPSON 3/8 ========================================= FIN

#========================= WINDOW METODO FALSA POSICIOM ========================================= INI
def window_falsa_posicion():
    global window_5
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = int(b)
            n = float(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_5, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_5, text=('Resultado Falsa posicion: ', falsa_posicion(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_5, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack()
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
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
            print("vacio: por favor ingrese todos los campos")
            

    window_5 = tk.Toplevel(root)
    window_5.geometry("800x400")
    window_5.title("Falsa posicion")
    
    lbl = tk.Label(window_5, text="El metodo de Falsa posicion...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_5, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_5, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_5, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_5, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_5, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_5, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_5, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_5, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_5, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO FALSA POSICIOM ========================================= FIN


#=============== WINDOW ABOUT US // ventana acerca de nosotros========================================= INI
def window_about_us():
    global window_aboutus
    window_aboutus = tk.Toplevel(root)
    window_aboutus.geometry("800x250")
    window_aboutus.title("Acerca de nosotros")
    lbl = tk.Label(window_aboutus, text="Calculadora Metodos Numericos, este proyecto implementa diversos metodos observados en el trancurso de la materia Metodos Numericos.\nProfesor: XXXXX \n Integrantes:\n Andres Duque 160003812\n Fredy Segura 1600038XX\n\n La mejor materia XD\n\n\n Y como dijo Diomedez tomese una cerveza y ...")
    lbl.pack(fill = BOTH, expand = 1)

    # # btn close window
    # btn_close =tk.Button(window_aboutus, text="Close window", command=lambda: window_aboutus.destroy())
    # btn_close.pack()
#=============== WINDOW ABOUT US // ventana acerca de nosotros========================================= FIN



#============================================= WINDOW GENERAL ========================================= INI
#
# assets of main window
#

# btn para ventana simpson 1/3
btn0 = tk.Button(root, text="Simpson 1/3", command=window_simpson_13)
btn0.pack(padx=5, pady=20)

# btn para ventana trapecios
btn1 = tk.Button(root, text="Trapecios", command=window_trapecios)
btn1.pack(padx=5, pady=5)

# btn para ventana 
btn2 = tk.Button(root, text="Biseccion", command=window_biseccion)
btn2.pack(padx=5, pady=5)

# btn para ventana 
btn3 = tk.Button(root, text="Simpson 3/8", command=window_simpson_38)
btn3.pack(padx=5, pady=5)

# btn para ventana falsa posicion
btn4 = tk.Button(root, text="Falsa Posicion", command=window_falsa_posicion)
btn4.pack(padx=5, pady=5)



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
#============================================= WINDOW GENERAL ========================================= FIN