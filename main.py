import tkinter as tk
import os as o
import time
from datetime import datetime, timedelta
root = tk.Tk()
root.title("Button Example")
root.geometry("600x400")
def shutDownComputer():
    print("Turning off Computer....")
    #o.system("shutdown /s /t 1")

def setTime(hours, minutes):
    integerHours = int(hours)
    integerMinutes = int(minutes)
    target_time = datetime.now() + timedelta(hours = integerHours, minutes=integerMinutes)
    checkTime(target_time)

def checkTime(target):
    if datetime.now() >= target:
        shutDownComputer()
    else:
        root.after(10000,lambda: checkTime(target))

def on_button_click():
    hours = text_boxHOURS.get("1.0", "end-1c")  # Get text from the Text widget
    minutes = text_boxMINUTES.get("1.0", "end-1c")  # Get text from the Text widget
    setTime(hours, minutes)


button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

text_boxHOURS = tk.Text(root, height = 1, width = 6)
text_boxHOURS.pack()

text_boxMINUTES = tk.Text(root, height = 1, width = 6)
text_boxMINUTES.pack()

root.mainloop()



