from os import path
import sys
from tkinter import font
# from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
sys.path.append("./")
from metodos.funciones import *
# 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.constants import BOTH
# 
# colocar iconos o imagenes en ventanas
from PIL import ImageTk,ImageTk, Image


root = tk.Tk()
# size de la ventana
root.geometry("500x500")
# configuracion de la ventana principal
root.title("Calculadora Metodos Numericos")
# # root.iconbitmap('c:/gui/codemy.ico')

# ========================= SCROLL BAR INI ======================================
def scroll_bar(window):
    # Create A Main Frame
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    # return the frame on the window you wanna use
    return second_frame
# ========================= SCROLL BAR FIN ======================================

# =======convierte un string a una funcion======================================
def string2func(string):
    ''' evalua el string y retorna una funcion de x '''
    replacements = {
        'sin' : 'np.sin',
        'cos' : 'np.cos',
        'exp': 'np.exp',
        '^': '**',
        'pi': 'np.pi'
    }

    for old, new in replacements.items():
        string = string.replace(old, new)
    # print(string)
    # return string

    def func(x):
        return eval(string)

    return func
# =======convierte un string a una funcion======================================


# ============= grafica una funcion dada INI ========================================
def graph(f, n, a, b):   
    x = np.linspace(a, b, n)
    # x = np.linspace(a, b)
    func = string2func(f)
    plt.plot(x, func(x))
    plt.xlim(a, b)
    plt.show()
# ============= grafica una funcion dada FIN ========================================

#========================= WINDOW metodo de simpson 1/3 ========================================= INI
def window_simpson_13():
    global window_1
   
    window_1 = tk.Toplevel(root)
    frame_1 = scroll_bar(window_1)
    window_1.geometry("500x500")
    window_1.title("Simpson 1/3")

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
            btn_graph = ttk.Button(frame_1, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(frame_1, text=('Resultado Simpson 1/3: ',simpson_13(a, b, n, func)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_1, text="Limipiar", command=lambda: var.set(1))
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
            # frame_1.destroy()
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
            

    # frame_1.resizable(False, False)
    lbl = tk.Label(frame_1, text="La regla de Simpson es un método de integración numérica.\nEn otras palabras, es la aproximación numérica de integrales definidas.\nLa regla de Simpson es la siguiente:\n\nEn ella:\nf(x) es llamado el integrand\na = es el límite inferior de integración\nb = es el límite superior de integración\n",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    # add image
    def add_img(path, y):
        img = PhotoImage(file=path)
        img_lbl =  ttk.Label(frame_1, image=img)
        img_lbl.image = img
        img_lbl.pack(pady=y)
        return img_lbl
    
    # img = add_img("C:/WSL/projectsU/project_metodos/assets/simpson_13/3.png", 10)
    img = add_img("assets/simpson_13/3.png", 10)
    # img_text.image_create(END, image=image_1)
    # img_text.pack()

    # img = ImageTk.PhotoImage(Image.open("C:/WSL/projectsU/project_metodos/assets/simpson_13/3.png"))
    # imglabel = Label(frame_1, image=img)
    # imglabel,image = img
    # imglabel.pack()

    # image = tk.PhotoImage(file="C:/WSL/projectsU/project_metodos/assets/simpson_13/2.png")
    # label = tk.Label(frame_1, image=image)
    # label.pack()

    # image1 = Image.open("C:/WSL/projectsU/project_metodos/assets/simpson_13/3.png")
    # test = ImageTk.PhotoImage(image1)

    # label1 = ttk.Label(frame_1, image=test)
    # label1.image = test

    # # Position image
    # label1.pack()

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_1, text = "funcion: ", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_1, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(frame_1, text = "a:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_1, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(frame_1, text = "b:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_1, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(frame_1, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_1, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    # for thing in range(100):
	#     Button(frame_1, text=f'Button {thing} Yo!').pack(side=tk.TOP, padx=5, pady=5)
    
    submit_btn = ttk.Button(frame_1, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
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
            btn_graph = ttk.Button(window_5, text="Graficar", command=lambda: graph(func, 20, a, b))
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

#========================= WINDOW METODO NEWTON-RAPHSON ========================================= INI
def window_newton_raphson():
    global window_6
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            b = int(b)
            n = float(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_6, text="Graficar", command=lambda: graph(func, 100, b, 20))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            # func=f, a=df, b=x0, n=tolerancia
            result_lbl = tk.Label(window_6, text=('Resultado Newton Raphson: ',newton_raphson(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_6, text="Limipiar", command=lambda: var.set(1))
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
            

    window_6 = tk.Toplevel(root)
    window_6.geometry("800x400")
    window_6.title("Newton Rapshon")
    
    lbl = tk.Label(window_6, text="El metodo de Newton Raphson...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_6, text = "f:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_6, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_6, text = "f':")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_6, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_6, text = "x0:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_6, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_6, text = "tolerancia:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_6, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_6, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO NEWTON-RAPHSON ========================================= FIN

#========================= WINDOW METODO SECANTE ========================================= INI
def window_secante():
    global window_7
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get() #  xa float
        n = n_d.get() # tolaera float
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = int(a)
            b = float(b)
            n = float(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_7, text="Graficar", command=lambda: graph(func, 20, a, 20))
            btn_graph.pack()

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(window_7, text=('Resultado Falsa posicion: ',secante(func, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_7, text="Limipiar", command=lambda: var.set(1))
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
            

    window_7 = tk.Toplevel(root)
    window_7.geometry("800x400")
    window_7.title("Secante")
    
    lbl = tk.Label(window_7, text="El metodo de Secante...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_7, text = "f:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_7, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_7, text = "a")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_7, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_7, text = "xa:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_7, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_7, text = "tolerancia:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_7, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_7, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO SECANTE ========================================= FIN

#========================= WINDOW METODO PUNTO FIJO ========================================= INI
def window_punto_fijo():
    global window_8
   
    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get()
        n = n_d.get()
        
        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = float(a)
            b = float(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_8, text="Graficar", command=lambda: graph(func, int(n), int(a), 20))
            btn_graph.pack()

            # 
            result_lbl = tk.Label(window_8, text=('Punto Fijo solucion: x ', punto_fijo(func, a, b, n)))
            result_lbl.pack(fill = BOTH)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(window_8, text="Limipiar", command=lambda: var.set(1))
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
            

    window_8 = tk.Toplevel(root)
    window_8.geometry("800x400")
    window_8.title("Punto Fijo")
    
    lbl = tk.Label(window_8, text="El metodo de Punto Fijo...")
    lbl.pack(fill = BOTH)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(window_8, text = "funcion:")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(window_8, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack()
    
    # a
    a_lbl = ttk.Label(window_8, text = "aprox:")
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(window_8, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack()
    # 

    # b
    b_lbl = ttk.Label(window_8, text = "tol:")
    b_lbl.pack()
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(window_8, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack()
    # 

    # n
    n_lbl = ttk.Label(window_8, text = "n:")
    n_lbl.pack()
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(window_8, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack()
    # 
    
    submit_btn = ttk.Button(window_8, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack()
#========================= WINDOW METODO PUNTO FIJO ========================================= FIN


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

# create scroll bar for main window
main_window = scroll_bar(root)

# btn para ventana simpson 1/3
btn0 = tk.Button(main_window, text="Simpson 1/3", command=window_simpson_13)
btn0.pack(fill = BOTH, pady=5)

# btn para ventana trapecios
btn1 = tk.Button(main_window, text="Trapecios", command=window_trapecios)
btn1.pack(padx=5, pady=5)

# btn para ventana 
btn2 = tk.Button(main_window, text="Biseccion", command=window_biseccion)
btn2.pack(padx=5, pady=5)

# btn para ventana 
btn3 = tk.Button(main_window, text="Simpson 3/8", command=window_simpson_38)
btn3.pack(padx=5, pady=5)

# btn para ventana falsa posicion
btn4 = tk.Button(main_window, text="Falsa Posicion", command=window_falsa_posicion)
btn4.pack(padx=5, pady=5)

# btn para ventana falsa posicion
btn5 = tk.Button(main_window, text="Newton Raphson", command=window_newton_raphson)
btn5.pack(padx=5, pady=5)

btn6 = tk.Button(main_window, text="Newton Raphson", command=window_newton_raphson)
btn6.pack(padx=5, pady=5)

btn7 = tk.Button(main_window, text="Punto Fijo", command=window_punto_fijo)
btn7.pack(padx=5, pady=5)


# btn para ventana acerca de nosotros
btn_about_us = tk.Button(
    main_window, text="Acerca de nosotros", command=window_about_us)
btn_about_us.pack(side=tk.BOTTOM, padx=20, pady=20)

# for thing in range(100):
# 	Button(main_window, text=f'Button {thing} Yo!').pack(side=tk.TOP, padx=150, pady=5)
# my_label = Label(main_window, text="It's Friday Yo!").pack(side=tk.RIGHT, padx=150, pady=5)


#
root.mainloop()
#============================================= WINDOW GENERAL ========================================= FIN