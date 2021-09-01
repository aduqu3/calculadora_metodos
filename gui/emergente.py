import tkinter as tk
import tkinter.ttk as ttk

from matplotlib.pyplot import text

# from PIL import ImageTk,ImageTk
# import numpy as np
# import matplotlib.pyplot as plt


# root.title("Calculadora")
# # root.iconbitmap('c:/gui/codemy.ico')
# root.geometry('400x200')

# def graph():
#     t = np.arange(0, 3, .01)
#     # ln(x) + sin(3x) + e^4
#     plt.plot(t, 2 * np.sin(2 * np.pi * t))
#     plt.show()

# btn = ttk.Button(root, text="graficar", command=graph)
# btn.grid(row=0, column=0)

# root.mainloop()

window_1 = ''
def openwindow():
    global window_1
    window_1 = tk.Toplevel(root)
    window_1.geometry("250x250")
    window_1.title("New window")
    window_1.resizable(False, False)
    lbl = tk.Label(window_1, text= "I'm the new window")
    lbl.pack()
    btn =tk.Button(window_1, text="Close me", command=lambda: window_1.destroy())
    btn.pack()

root = tk.Tk()

btn = tk.Button(root, text="Open New Window", command=openwindow)
btn.pack(padx=20, pady=20)

# tk.Button(root, text="Close new ")

root.geometry("500x500")
root.mainloop()