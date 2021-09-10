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
    # x = np.linspace(a, b, n)
    x = np.linspace(a, b)
    func = string2func(f)
    plt.plot(x, func(x))
    plt.xlim(a, b)
    plt.show()
# ============= grafica una funcion dada FIN ========================================

# ============= ADD IMAGE INI ========================================
def add_img(path, frame, y, img_x=1, img_y=1, x=0):
    img = PhotoImage(file=path)
    img = img.subsample(img_x, img_y)
    img_lbl =  ttk.Label(frame, image=img)
    img_lbl.image = img
    img_lbl.pack(padx=x, pady=y)
    return img_lbl
# ============= ADD IMAGE FIN ========================================

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
            btn_graph.pack(pady=10)

            # luego llamar metodo simpson 1/3
            # y mostrar el resultado en la ventana
            result_lbl = tk.Label(frame_1, text=('Resultado Simpson 1/3: ',simpson_13(a, b, n, func)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_1, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
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
            
    title_lbl = tk.Label(frame_1, text="Regla de Simpson 1/3\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    # frame_1.resizable(False, False)
    lbl = tk.Label(frame_1, text="La regla de Simpson es un método de integración numérica.\nEn otras palabras, es la aproximación numérica de integrales definidas.\nLa regla de Simpson es la siguiente:\n\nEn ella:\nf(x) es llamado el integrand\na = es el límite inferior de integración\nb = es el límite superior de integración\n",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/simpson_13/1.png", frame_1, 10, 2, 2)

    
    lbl2 = tk.Label(frame_1, text="Como se muestra en el diagrama anterior, el integrando f(x) es aproximado\npor un polinomiode segundo orden, el interpolante cuadrático es P(x).\nsigue la aproximación:\n",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/simpson_13/2.png", frame_1, 10)

    lbl3 = tk.Label(frame_1, text="Reemplazando (b-a)/2 como h, obtenemos", font=("Helvetica", 11), justify="left")
    lbl3.pack(fill = BOTH, pady=10)
    
    img3 = add_img("assets/simpson_13/3.png", frame_1, 10)

    lbl4 = tk.Label(frame_1, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    lbl4.pack(fill = BOTH, pady=10)


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
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_1, text = "a:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_1, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_1, text = "b:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_1, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_1, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_1, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
    
    # for thing in range(100):
	#     Button(frame_1, text=f'Button {thing} Yo!').pack(side=tk.TOP, padx=5, pady=5)
    
    submit_btn = ttk.Button(frame_1, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW metodo de simpson 1/3 ========================================= FIN

#========================= WINDOW METODO TRAPECIOS ========================================= INI
def window_trapecios():
    global window_2
   
    window_2 = tk.Toplevel(root)
    frame_2 = scroll_bar(window_2)
    window_2.geometry("500x500")
    window_2.title("Trapecios")

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
            btn_graph = ttk.Button(frame_2, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_2, text=('Resultado Trapecios: ',trapecios(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_2, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_2.destroy()
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
            

    title_lbl = tk.Label(frame_2, text="Regla de Trapecios\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_2, text="En análisis numérico la regla del trapecio es un método de integración, es decir,\nun método para calcular aproximadamente el valor de una integral definida.\nLa regla se basa en aproximar el valor de la integral de f(x) porel de la función lineal,\n que pasa a través de los puntos (a,f(a)) y (b,f(b)).\nLa integral de ésta es igual al área del trapecio bajo la gráfica de la función lineal.\n",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/trapecios/0.png", frame_2, 10, 2, 2)

    
    lbl2 = tk.Label(frame_2, text="Regla de trapecio simple:\nPara realizar la aproximación por esta regla es necesario usar un polinomio de primer orden,\n y esta es representada por:\n",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/trapecios/1.png", frame_2, 10)

    lbl4 = tk.Label(frame_2, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    lbl4.pack(fill = BOTH, pady=10)


    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_2, text = "funcion: ", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_2, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_2, text = "a:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_2, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_2, text = "b:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_2, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_2, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_2, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
    
    # for thing in range(100):
	#     Button(frame_2, text=f'Button {thing} Yo!').pack(side=tk.TOP, padx=5, pady=5)
    
    submit_btn = ttk.Button(frame_2, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO TRAPECIOS ========================================= FIN

#========================= WINDOW METODO BISECCION ========================================= INI
def window_biseccion():
    global window_3
   
    window_3 = tk.Toplevel(root)
    frame_3 = scroll_bar(window_3)
    window_3.geometry("500x500")
    window_3.title("Biseccion")

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
            btn_graph = ttk.Button(frame_3, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_3, text=('Resultado Biseccion: ',bisection(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_3, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_3.destroy()
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
            
    title_lbl = tk.Label(frame_3, text="Biseccion\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_3, text="El método de bisección es uno de los más versátiles para determinar una raíz real\nen un intervalo de una ecuación dada, es fácil de comprender, aunque si se desea una mayor\nexactitud el número de cálculos que hay que realizar aumenta considerablemente.\n\nUna de sus ventajas es que funciona para ecuaciones algebraicas y trascendentes,\npero se recomienda utilizarlo después de un análisis gráfico.\n\nEl Teorema de Bolzano establece las condiciones necesarias \npara la existencia de al menos un cero de una función continua.",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

        
    lbl2 = tk.Label(frame_3, text="Teorema de Bolzano\nSi f(x) es continua en el intervalo [a,b], con f(a)∙f(b)<0,\n entonces existe al menos un c∈]a,b[ tal que f(c)=0.\n\nEl método de bisección se basa en el Teorema de Bolzano, el cual afirma que si se\ntiene una función real y=f(x) continua en el intervalo ]a,b[ donde el signo \nde la función en el extremo a es distinto al signo de la función en el extremo b del intervalo, \nentonces existe al menos un c∈]a,b[ tal que f(c)=0, que es la raíz buscada.",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)


    img = add_img("assets/biseccion/0.png", frame_3, 10)

    lbl4 = tk.Label(frame_3, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    lbl4.pack(fill = BOTH, pady=10)


    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_3, text = "funcion: ", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_3, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_3, text = "a:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_3, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_3, text = "b:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_3, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_3, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_3, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_3, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO BISECCION ========================================= FIN

#========================= WINDOW METODO SIMPSON 3/8 ========================================= INI
def window_simpson_38():
    global window_4
   
    window_4 = tk.Toplevel(root)
    frame_4 = scroll_bar(window_4)
    window_4.geometry("500x500")
    window_4.title("Simpson 3/8")

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
            btn_graph = ttk.Button(frame_4, text="Graficar", command=lambda: graph(func, n, a, b))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_4, text=('Resultado Simpson 3/8: ', simpson_38(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_4, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_4.destroy()
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
            
    title_lbl = tk.Label(frame_4, text="Regla de Simpson 3/8\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_4, text="La regla de 3/8 de Simpson es similar a la regla de 1/3 de Simpson, con la única diferencia\n de que, para la regla de 3/8, el interpolante es un polinomio cúbico.\n Aunque la regla de 3/8 utiliza un valor de función más, es aproximadamente \ndos veces más precisa que la regla de 1/3.\n",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/simpson_38/0.png", frame_4, 10)

        
    lbl2 = tk.Label(frame_4, text="La regla de 3/8 de Simpson establece:",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)


    img1 = add_img("assets/simpson_38/1.png", frame_4, 10)
    
    lbl3 = tk.Label(frame_4, text="Reemplazando (b-a)/3 como h, obtenemos,",
    font=("Helvetica", 11), justify="left")
    lbl3.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/simpson_38/2.png", frame_4, 10)

    lbl4 = tk.Label(frame_4, text="La regla de 3/8 de Simpson para n intervalos (n debería ser un múltiplo de 3):",
    font=("Helvetica", 11), justify="left")
    lbl4.pack(fill=BOTH, pady=10)

    img3 = add_img("assets/simpson_38/3.png", frame_4, 10)

    lbl5 = tk.Label(frame_4, text="donde xj = a+jh para j = 0,1,…,n-1,n con h=(b-a)/n; en particular, x0 = a y xn = b.",
    font=("Helvetica", 11), justify="left")
    lbl5.pack(fill=BOTH, pady=10)

    lbl6 = tk.Label(frame_4, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    lbl6.pack(fill = BOTH, pady=10)


    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_4, text = "funcion: ", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_4, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_4, text = "a:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_4, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_4, text = "b:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_4, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_4, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_4, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_4, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO SIMPSON 3/8 ========================================= FIN

#========================= WINDOW METODO FALSA POSICIOM ========================================= INI
def window_falsa_posicion():
    global window_5
   
    window_5 = tk.Toplevel(root)
    frame_5 = scroll_bar(window_5)
    window_5.geometry("500x500")
    window_5.title("Falsa posicion")

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
            btn_graph = ttk.Button(frame_5, text="Graficar", command=lambda: graph(func, 20, a, b))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_5, text=('Resultado Falsa posicion: ', falsa_posicion(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_5, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_5.destroy()
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
            
    title_lbl = tk.Label(frame_5, text="Falsa Posicion\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_5, text="La falsa posición es una alternativa a la bisección basada en una visualización gráfica.\nUn inconveniente del método de bisección es que al dividir el intervalo de xl \na xu en mitades iguales, no se toman en consideración las magnitudes de f(xl) y f(xu). \nPor ejemplo, si f(xl) está mucho más cercana a cero que f(xu), es lógico que la raíz \nse encuentre más cerca de xl que de xu. Un método alternativo que aprovecha \nesta visualización gráfica consiste en unir f(xl) y f(xu) con una línea recta. \nLa intersección de esta línea con el eje de las x representa una mejor aproximación de la raíz. \nEl hecho de que se reemplace la curva por una línea recta da una “falsa posición” \nde la raíz; de aquí el nombre de método de la falsa posición, o en latín, regula falsi. \nTambién se le conoce como método de interpolación lineal.\n",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/falsa_posicion/1.png", frame_5, 10, 2, 2)

        
    lbl2 = tk.Label(frame_5, text="Usando triángulos semejantes, la intersección de la línea recta con el eje de las x se estima \nmediante una semejanza de triángulos, en la cual se despeja xr",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/falsa_posicion/2.png", frame_5, 10, 2, 2)
    
    test_lbl = tk.Label(frame_5, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_5, text = "funcion: ", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_5, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_5, text = "a:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_5, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_5, text = "b:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_5, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_5, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_5, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_5, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO FALSA POSICIOM ========================================= FIN

#========================= WINDOW METODO NEWTON-RAPHSON ========================================= INI
def window_newton_raphson():
    global window_6
   
    window_6 = tk.Toplevel(root)
    frame_6 = scroll_bar(window_6)
    window_6.geometry("500x500")
    window_6.title("Newton Rapshon")

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
            btn_graph = ttk.Button(frame_6, text="Graficar", command=lambda: graph(func, 100, b, 20))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_6, text=('Resultado Newton Rapshon: ', newton_raphson(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_6, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_6.destroy()
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
            
    title_lbl = tk.Label(frame_6, text="Newton Rapshon\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_6, text="El método de Newton-Rhapson es uno de los más utilizados para dar solución a \necuaciones algebraicas y trascendentes. Clasificándose entre los métodos abiertos, es decir, \naquellos que requieren uno o dos valores que no necesariamente encierren a la raíz.\n\n El método de Newton-Raphson se deduce a partir de esta interpretación geométrica y \nse tiene que la primera derivada en x es equivalente a la pendiente:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/newton_raphson/1.png", frame_6, 10)

    lbl2 = tk.Label(frame_6, text="Que se arregla para obtener", font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/newton_raphson/2.png", frame_6, 10)

    lbl3 = tk.Label(frame_6, text="Mientras que el error aproximado porcentual lo calcularemos con la siguiente fórmula:", font=("Helvetica", 11), justify="left")
    lbl3.pack(fill=BOTH, pady=10)

    img3 = add_img("assets/newton_raphson/3.png", frame_6, 10)
    
    test_lbl = tk.Label(frame_6, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_6, text = "f:", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_6, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_6, text = "f':", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_6, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_6, text = "x0:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_6, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_6, text = "tolerancia:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_6, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_6, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO NEWTON-RAPHSON ========================================= FIN

#========================= WINDOW METODO SECANTE ========================================= INI
def window_secante():
    global window_7
   
    window_7 = tk.Toplevel(root)
    frame_7 = scroll_bar(window_7)
    window_7.geometry("500x500")
    window_7.title("Secante")

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
            btn_graph = ttk.Button(frame_7, text="Graficar", command=lambda: graph(func, 20, a, 20))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_7, text=('Resultado Secante: ', secante(func, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_7, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_7.destroy()
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
            
    title_lbl = tk.Label(frame_7, text="Secante\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_7, text="El principal inconveniente del método de Newton estriba en que requiere conocer \nel valor de la primera derivada de la función en el punto. Sin embargo, \nla forma funcional de f(x) dificulta en ocasiones el cálculo de la derivada. \nEn estos casos es más útil emplear el método de la secante.\n\nEl método de la secante parte de dos puntos (y no sólo uno como el método de Newton)\ny estima la tangente (es decir, la pendiente de la recta) por una aproximación \nde acuerdo con la expresión:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/secante/1.png", frame_7, 10)

    lbl2 = tk.Label(frame_7, text="Sustituyendo esta expresión en la ecuación (29) del método de Newton, obtenemos \nla expresión del método de la secante que nos proporciona el siguiente punto de iteración:", font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/secante/2.png", frame_7, 10)
    img3 = add_img("assets/secante/3.png", frame_7, 10)
    
    test_lbl = tk.Label(frame_7, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_7, text = "f:", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_7, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_7, text = "a", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_7, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_7, text = "xa:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_7, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_7, text = "tolerancia:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_7, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_7, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO SECANTE ========================================= FIN

#========================= WINDOW METODO PUNTO FIJO ========================================= INI
def window_punto_fijo():
    global window_8
   
    window_8 = tk.Toplevel(root)
    frame_8 = scroll_bar(window_8)
    window_8.geometry("500x500")
    window_8.title("Punto Fijo")

    def press(func_d, a_d, b_d, n_d,):
        func = func_d.get()
        a = a_d.get()
        b = b_d.get() #  xa float
        n = n_d.get() # tolaera float

        if( len(func) and len(a) and len(b) and len(n)):
            # print("vamos a hacer algo")
            a = float(a)
            b = float(b)
            n = int(n)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad
           
            # btn graficar ecuacion
            btn_graph = ttk.Button(frame_8, text="Graficar", command=lambda: graph(func, int(n), int(a), 20))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_8, text=('Punto Fijo solucion: x ', punto_fijo(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_8, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            btn_graph.destroy()
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_8.destroy()
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
            
    title_lbl = tk.Label(frame_8, text="Punto Fijo\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    lbl = tk.Label(frame_8, text="Dada una ecuación f(x) = 0, podemos transformarla, de alguna manera, en otra \nequivalente del tipo x = g(x) para alguna función g. En este caso se tiene que: \na es raíz de f(x) = 0 ↔ f(a) = 0 ↔ a = g(a) ↔ a es raíz de x = g(x).\n\nDefinición:\n\nUn número a tal que a = g(a) se dice un punto fijo de la función g.\nCuándo una función g tiene un punto fijo, y si lo tiene, cómo encontrarlo?\n\nTeorema de punto fijo:\n\nSi g es una función continua en [a, b] y g(x) ε[a, b] para todo x ε[a, b], \nentonces g tiene por lo menos un punto fijo en [a, b]. Si además, \ng’(x) existe para todo x ε[a, b], y |g’(x)| ≤ K < 1 para todo x ε[a, b], K constante, \nentonces g tiene un único punto fijo x ε[a, b]. La sucesión {xn}, con n definida, \nse encuentra mediante la fórmula de iteración:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/punto_fijo/1.png", frame_8, 10, 2, 2)
    
    test_lbl = tk.Label(frame_8, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_8, text = "funcion:", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_8, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_8, text = "aprox:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_8, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_8, text = "tol:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_8, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_8, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_8, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_8, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW METODO PUNTO FIJO ========================================= FIN

#========================= WINDOW TIPOS DE ERRORES ========================================= INI
def window_errores():
    global window_9
   
    window_9 = tk.Toplevel(root)
    frame_9 = scroll_bar(window_9)
    window_9.geometry("500x500")
    window_9.title("Tipos de Errores")

    def press(a_d, b_d):
        a = a_d.get()
        b = b_d.get()

        if( len(a) and len(b) ):
            # print("vamos a hacer algo")
            a = float(a)
            b = float(b)
            
            # procesar la info y vaciar el StringVar tk_string, para que no se muestre nuevamente
            # la funcion ingresada con anterioridad

            result_1_lbl = tk.Label(frame_9, text=error_verdadero(a, b), font=("Helvetica", 14))
            result_1_lbl.pack(fill = BOTH, pady=10)

            result_1_lbl = tk.Label(frame_9, text=error_relativo(a, b), font=("Helvetica", 14))
            result_1_lbl.pack(fill = BOTH, pady=10)

            result_1_lbl = tk.Label(frame_9, text=error_aproximado(b, a), font=("Helvetica", 14))
            result_1_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_9, text="Limipiar", command=lambda: var.set(1))
            btn_clean.pack(pady=10)
            # btn_clean.place(relx=.5, rely=.5, anchor="c")

            # print("waiting...")
            btn_clean.wait_variable(var)
            # print("done waiting.")

            # limpiar variables // destruir elementos
            result_lbl.destroy()
            btn_clean.destroy()
            # btn_clean.destroy()
            # frame_9.destroy()
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

    # ++++++++++++++++++++++ INI 
    title_lbl = tk.Label(frame_9, text="Tipos de Errores\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH, pady=10)

    # error absoluto
    lbl = tk.Label(frame_9, text="Error absoluto:\nEs la diferencia entre el valor de la medida y el valor tomado como exacto.\nPuede ser positivo o negativo, según si la medida es superior al valor real o \ninferior (la resta sale positiva o negativa). Tiene unidades, \nlas mismas que las de la medida.",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH, pady=10)

    img = add_img("assets/errores/0.png", frame_9, 10)

    # error relativo
    lbl1 = tk.Label(frame_9, text="Error relativo.\nEs el cociente (la división) entre el error absoluto y el valor exacto. Si se multiplica \npor 100 se obtiene el tanto por ciento (%) de error. Al igual que el error absoluto \npuede ser positivo o negativo (según lo sea el error absoluto) porque puede ser \npor exceso o por defecto. no tiene unidades.",
    font=("Helvetica", 11), justify="left")
    lbl1.pack(fill = BOTH, pady=10)

    img1 = add_img("assets/errores/1.png", frame_9, 10)

    # error aproximado
    lbl2 = tk.Label(frame_9, text="Error de aproximación:\nLa incertidumbre o error numérico es una medida del ajuste o cálculo de una \nmagnitud con respecto al valor real o teórico que dicha magnitud tiene. \nUn aspecto importante de los errores de aproximación es su estabilidad numérica. \nDicha estabilidad se refiere a cómo dentro de un algoritmo de análisis \nnumérico el error de aproximación es propagado dentro del propio algoritmo.",
    font=("Helvetica", 11), justify="left")
    lbl2.pack(fill = BOTH, pady=10)

    img2 = add_img("assets/errores/2.png", frame_9, 10)

    # error verdadero
    lbl3 = tk.Label(frame_9, text="Error verdadero:\nEl valor verdadero obtenido en una aproximación se define como:",
    font=("Helvetica", 11), justify="left")
    lbl3.pack(fill = BOTH, pady=10)

    img3 = add_img("assets/errores/3.png", frame_9, 10)
    
    # texto probarr metodo
    test_lbl = tk.Label(frame_9, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)
    # ++++++++++++++++++++++ FIN
    
    # INPUTS
    # a
    a_lbl = ttk.Label(frame_9, text = "valor real:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_9, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_9, text = "valor aproximado:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_9, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_9, text = "calcular", command=lambda: press(a_str, b_str))
    submit_btn.pack(pady=10)
#========================= WINDOW TIPOS DE ERRORES ========================================= FIN


#=============== WINDOW ABOUT US // ventana acerca de nosotros========================================= INI
def window_about_us():
    global window_aboutus
    window_aboutus = tk.Toplevel(root)
    window_aboutus.geometry("800x250")
    window_aboutus.title("Acerca de nosotros")
    lbl = tk.Label(window_aboutus, text="Calculadora Metodos Numericos, este proyecto implementa diversos metodos observados en el trancurso de la materia Metodos Numericos.\nProfesor: Caillo Torres Gomez\nIntegrantes:\n Andres Duque 160003812\n Fredy Segura 160003830\n")
    lbl.pack(fill = BOTH, expand = 1)
#=============== WINDOW ABOUT US // ventana acerca de nosotros========================================= FIN



#============================================= WINDOW GENERAL ========================================= INI
# create scroll bar for main window
main_window = scroll_bar(root)

# btn para ventana simpson 1/3
btn0 = tk.Button(main_window, text="Simpson 1/3", command=window_simpson_13)
btn0.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

# btn para ventana trapecios
btn1 = tk.Button(main_window, text="Trapecios", command=window_trapecios)
btn1.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

# btn para ventana 
btn2 = tk.Button(main_window, text="Biseccion", command=window_biseccion)
btn2.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

# btn para ventana 
btn3 = tk.Button(main_window, text="Simpson 3/8", command=window_simpson_38)
btn3.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

# btn para ventana falsa posicion
btn4 = tk.Button(main_window, text="Falsa Posicion", command=window_falsa_posicion)
btn4.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

# btn para ventana falsa posicion
btn5 = tk.Button(main_window, text="Newton Raphson", command=window_newton_raphson)
btn5.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

btn6 = tk.Button(main_window, text="Secante", command=window_secante)
btn6.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

btn7 = tk.Button(main_window, text="Punto Fijo", command=window_punto_fijo)
btn7.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)

btn8 = tk.Button(main_window, text="Tipos de errores", command=window_errores)
btn8.pack(side=tk.TOP, fill = BOTH, padx=10, pady=5)


# btn para ventana acerca de nosotros
btn_about_us = tk.Button(
    main_window, text="Acerca de nosotros", command=window_about_us)
btn_about_us.pack(side=tk.BOTTOM, padx=10, pady=20)

# for thing in range(100):
# 	Button(main_window, text=f'Button {thing} Yo!').pack(side=tk.TOP, padx=150, pady=5)
# my_label = Label(main_window, text="It's Friday Yo!").pack(side=tk.RIGHT, padx=150, pady=5)


#
root.mainloop()
#============================================= WINDOW GENERAL ========================================= FIN