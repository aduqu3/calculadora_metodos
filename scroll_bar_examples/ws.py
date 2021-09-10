import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

root = tk.Tk()

# # Create A Main Frame
# main_frame = Frame(root)
# main_frame.pack(fill=BOTH, expand=1)
# # Create A Canvas
# my_canvas = Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# # Add A Scrollbar To The Canvas
# my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)
# # Configure The Canvas
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
# # Create ANOTHER Frame INSIDE the Canvas
# second_frame = Frame(my_canvas)
# # Add that New frame To a Window In The Canvas
# my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# i need to create another frame



# for thing in range(100):
# 	Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)
# my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)

def scroll_bar(window):
    # 
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
    # 
    return second_frame



def window_about_us():
    global window_aboutus
    window_aboutus = tk.Toplevel(root)
    second_frame = scroll_bar(window_aboutus)

    window_aboutus.geometry("800x100")
    window_aboutus.title("Acerca de nosotros")
    lbl = tk.Label(second_frame, text="Calculadora Metodos Numericos, este proyecto implementa diversos metodos observados en el trancurso de la materia Metodos Numericos.\nProfesor: XXXXX \n Integrantes:\n Andres Duque 160003812\n Fredy Segura 1600038XX\n\n La mejor materia XD\n\n\n Y como dijo Diomedez tomese una cerveza y ...")
    lbl.pack(fill = BOTH, expand = 1)

   

    # # btn close window
    # btn_close =tk.Button(window_aboutus, text="Close window", command=lambda: window_aboutus.destroy())
    # btn_close.pack()
#=============== WINDOW ABOUT US // ventana acerca de nosotros========================================= FIN


frame_1 = scroll_bar(root)

btn_about_us = tk.Button(
    frame_1, text="Acerca de nosotros", command=window_about_us)
btn_about_us.pack(padx=20, pady=20)
btn_about_us2 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us3 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us4 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us5 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us6 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us7 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us8 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us9 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us10 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us12 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us12 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us13 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us14 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us15 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us21 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us22 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us23 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us24 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us25 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
btn_about_us26 = tk.Button(frame_1, text="Acerca de nosotros").pack(padx=5, pady=5)
# btn1 = tk.Button(root, text="Simpson 1/3", command=openwindow)
# btn1.pack(padx=20, pady=20)

# size de la ventana
root.geometry("500x300")
# configuracion de la ventana principal
root.title("Calculadora Metodos Numericos")
# # root.iconbitmap('c:/gui/codemy.ico')
# root.geometry('400x200')
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill=Y )

# root.title('Learn To Code at Codemy.com')
# #root.iconbitmap('c:/gui/codemy.ico')
# root.geometry("500x400")


root.mainloop()