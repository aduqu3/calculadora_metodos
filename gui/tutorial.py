from tkinter.constants import BOTH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import tkinter as tk
import tkinter.ttk as ttk

# colocar iconos o imagenes en ventanas
# from PIL import ImageTk,ImageTk

root = tk.Tk()

# graficar funciones

# graficar ecuacion


def graph():
    t = np.arange(0, 3, .01)
    # ln(x) + sin(3x) + e^4
    plt.plot(t, 2 * np.sin(2 * np.pi * t))
    plt.show()



#===============metodo de simpson=========================================INICIO
def window_simpson_13():
    global window_1
    
    def press(str):
        print(str.get())
        if(str.get()==''):
            print("esta vacio")
        else:
            # print("no esta vacio")
            # btn graficar ecuacion
            btn_graph = ttk.Button(window_1, text="Graficar", command=graph)
            btn_graph.pack()

    global window_1
    window_1 = tk.Toplevel(root)
    window_1.geometry("800x250")
    window_1.title("Simpson 1/31")
    # window_1.resizable(False, False)
    lbl = tk.Label(window_1, text="El metodo de simpson 1/3...")
    lbl.pack(fill = BOTH)

    # colocar label para el input
    # input text
    user_password = ttk.Label(window_1, text = "Password")
    user_password.pack()

    # input text


    # cada vez que presione los captura...
    # expr = ''
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
#===============metodo de simpson=========================================FIN



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
