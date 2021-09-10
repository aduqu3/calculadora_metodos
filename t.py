#========================= WINDOW TIPOS DE ERRORES ========================================= INI
def window_errores():
    global window_9
   
    window_9 = tk.Toplevel(root)
    frame_9 = scroll_bar(window_9)
    window_9.geometry("500x500")
    window_9.title("Punto Fijo")

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
            btn_graph = ttk.Button(frame_9, text="Graficar", command=lambda: graph(func, int(n), int(a), 20))
            btn_graph.pack(pady=10)

            result_lbl = tk.Label(frame_9, text=('Punto Fijo solucion: x ', punto_fijo(func, a, b, n)), font=("Helvetica", 14))
            result_lbl.pack(fill = BOTH, pady=10)

            # btn para limpiar la interfaz luego de realizar un calculo
            var = tk.IntVar()
            btn_clean = ttk.Button(frame_9, text="Limipiar", command=lambda: var.set(1))
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
            
    title_lbl = tk.Label(frame_9, text="Punto Fijo\n",
    font=("Helvetica", 14), justify="left")
    title_lbl.pack(fill = BOTH)

    lbl = tk.Label(frame_9, text="Dada una ecuación f(x) = 0, podemos transformarla, de alguna manera, en otra \nequivalente del tipo x = g(x) para alguna función g. En este caso se tiene que: \na es raíz de f(x) = 0 ↔ f(a) = 0 ↔ a = g(a) ↔ a es raíz de x = g(x).\n\nDefinición:\n\nUn número a tal que a = g(a) se dice un punto fijo de la función g.\nCuándo una función g tiene un punto fijo, y si lo tiene, cómo encontrarlo?\n\nTeorema de punto fijo:\n\nSi g es una función continua en [a, b] y g(x) ε[a, b] para todo x ε[a, b], \nentonces g tiene por lo menos un punto fijo en [a, b]. Si además, \ng’(x) existe para todo x ε[a, b], y |g’(x)| ≤ K < 1 para todo x ε[a, b], K constante, \nentonces g tiene un único punto fijo x ε[a, b]. La sucesión {xn}, con n definida, \nse encuentra mediante la fórmula de iteración:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/punto_fijo/1.png", frame_9, 10, 2, 2)
    
    test_lbl = tk.Label(frame_9, text="Probar metodo:", font=("Helvetica", 11), justify="left")
    test_lbl.pack(fill = BOTH, pady=10)

    # func
    # colocar label para el input
    func_lbl = ttk.Label(frame_9, text = "funcion:", font=("Helvetica", 11), justify="left")
    func_lbl.pack()
    # se crea un entry, para el ingreso de texto desde teclado
    # luego guardamos esa informacion dentro de un StringVar tk_string
    func_str = tk.StringVar()
    func_inp = ttk.Entry(frame_9, textvariable=func_str)
    func_inp.configure(background="white")
    func_inp.focus()
    func_inp.pack(pady=10)
    
    # a
    a_lbl = ttk.Label(frame_9, text = "aprox:", font=("Helvetica", 11))
    a_lbl.pack()
    
    a_str = tk.StringVar()
    a_inp = ttk.Entry(frame_9, textvariable=a_str)
    a_inp.configure(background="white")
    a_inp.focus()
    a_inp.pack(pady=10)
    # 

    # b
    b_lbl = ttk.Label(frame_9, text = "tol:", font=("Helvetica", 11))
    b_lbl.pack(pady=10)
    
    b_str = tk.StringVar()
    b_inp = ttk.Entry(frame_9, textvariable=b_str)
    b_inp.configure(background="white")
    b_inp.focus()
    b_inp.pack(pady=10)
    # 

    # n
    n_lbl = ttk.Label(frame_9, text = "n:", font=("Helvetica", 11))
    n_lbl.pack(pady=10)
    
    n_str = tk.StringVar()
    n_inp = ttk.Entry(frame_9, textvariable=n_str)
    n_inp.configure(background="white")
    n_inp.focus()
    n_inp.pack(pady=10)
    # 
        
    submit_btn = ttk.Button(frame_9, text = "calcular", command=lambda: press(func_str, a_str, b_str, n_str))
    submit_btn.pack(pady=10)
#========================= WINDOW TIPOS DE ERRORES ========================================= FIN