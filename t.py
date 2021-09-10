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
    title_lbl.pack(fill = BOTH)

    lbl = tk.Label(frame_8, text="El principal inconveniente del método de Newton estriba en que requiere conocer \nel valor de la primera derivada de la función en el punto. Sin embargo, \nla forma funcional de f(x) dificulta en ocasiones el cálculo de la derivada. \nEn estos casos es más útil emplear el método de la secante.\n\nEl método de la secante parte de dos puntos (y no sólo uno como el método de Newton)\ny estima la tangente (es decir, la pendiente de la recta) por una aproximación \nde acuerdo con la expresión:",
    font=("Helvetica", 11), justify="left")
    lbl.pack(fill = BOTH)

    img = add_img("assets/secante/1.png", frame_8, 10)

    lbl2 = tk.Label(frame_8, text="Sustituyendo esta expresión en la ecuación (29) del método de Newton, obtenemos \nla expresión del método de la secante que nos proporciona el siguiente punto de iteración:", font=("Helvetica", 11), justify="left")
    lbl2.pack(fill=BOTH, pady=10)

    img2 = add_img("assets/secante/2.png", frame_8, 10)
    img3 = add_img("assets/secante/3.png", frame_8, 10)
    
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