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

            result_lbl = tk.Label(frame_7, text=('Resultado Newton Rapshon: ', secante(func, b, n)), font=("Helvetica", 14))
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
    title_lbl.pack(fill = BOTH)

    lbl = tk.Label(frame_7, text="El método de Newton-Rhapson es uno de los más utilizados para dar solución a \necuaciones algebraicas y trascendentes. Clasificándose entre los métodos abiertos, es decir, \naquellos que requieren uno o dos valores que no necesariamente encierren a la raíz.\n\n El método de Newton-Raphson se deduce a partir de esta interpretación geométrica y \nse tiene que la primera derivada en x es equivalente a la pendiente:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/newton_raphson/1.png", frame_7, 10)

    lbl2 = tk.Label(frame_7, text="Que se arregla para obtener", font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/newton_raphson/2.png", frame_7, 10)

    lbl3 = tk.Label(frame_7, text="Mientras que el error aproximado porcentual lo calcularemos con la siguiente fórmula:", font=("Helvetica", 11), justify="left")
    lbl3.pack(fill=BOTH, pady=10)

    img3 = add_img("assets/newton_raphson/1.png", frame_7, 10)
    
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