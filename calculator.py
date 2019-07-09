import tkinter as tk
from tkinter import messagebox

mainwindow = tk.Tk()
mainwindow.title("calculator")

heading_label_1 = tk.Label(mainwindow, text="Enter first value")
heading_label_1.pack()
name_field1 = tk.Entry(mainwindow)
name_field1.pack()

heading_label_2 = tk.Label(mainwindow, text="Enter second value")
heading_label_2.pack()
name_field2 = tk.Entry(mainwindow)
name_field2.pack()

heading_label_3 = tk.Label(mainwindow, text="operators")
heading_label_3.pack()

def takeValueInput():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    sum = var1 + var2
    print(sum)

button = tk.Button(mainwindow, text="+", command=lambda: takeValueInput())
button.pack()

def takeValueInput2():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    if var1 < var2:
        messagebox.showerror("error", "first number has smaller value then second number")
    else:
        diff = var1 - var2
        print(diff)

button = tk.Button(mainwindow, text="-", command=lambda: takeValueInput2())
button.pack()


def takeValueInput3():
    var1 = int(name_field1.get())
    var2 = int(name_field2.get())
    mul = var1 * var2
    print(mul)

button = tk.Button(mainwindow, text="*", command=lambda: takeValueInput3())
button.pack()


def takeValueInput4():
    var1 = float(name_field1.get())
    var2 = float(name_field2.get())
    if var2 == 0:
        messagebox.showerror("error", "number could not be divide by zero")
    else:
        div = var1 / var2
        print(div)

button = tk.Button(mainwindow, text="/", command=lambda: takeValueInput4())
button.pack()

mainwindow.mainloop()