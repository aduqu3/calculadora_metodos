import tkinter as tk
import tkinter.ttk as ttk

from PIL import ImageTk,ImageTk
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Calculadora")
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry('400x200')

def graph():
    t = np.arange(0, 3, .01)
    # ln(x) + sin(3x) + e^4
    plt.plot(t, 2 * np.sin(2 * np.pi * t))
    plt.show()

btn = ttk.Button(root, text="graficar", command=graph)
btn.grid(row=0, column=0)

root.mainloop()
