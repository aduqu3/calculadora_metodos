#===============metodo de simpson 1/3=========================================INICIO
def window_simpson_13(ttk, tk,):
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