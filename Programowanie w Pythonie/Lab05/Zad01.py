# Powinno być git już działa tylko na całkowitych
import tkinter as tk
from tkinter import font, RAISED, E
import re

x = "0"
start = True
dec = True

def change_to_bin():
    global x
    global  dec
    if dec == True:
        splitet = re.split('([-+/*])', x)
        if splitet[0] == '':
            splitet.remove("")
        for i in range(len(splitet)):
            znaki = ["+", "-", "*", "/"]
            if all(z not in splitet[i] for z in znaki):
                splitet[i] = bin(int(splitet[i]))[2:]
        x = ""
        x = "".join(splitet)
        var.set(x)
        button2['bg'] = "grey"
        button3['bg'] = "grey"
        button4['bg'] = "grey"
        button5['bg'] = "grey"
        button6['bg'] = "grey"
        button7['bg'] = "grey"
        button8['bg'] = "grey"
        button9['bg'] = "grey"
        button2["state"] = "disabled"
        button3["state"] = "disabled"
        button4["state"] = "disabled"
        button5["state"] = "disabled"
        button6["state"] = "disabled"
        button7["state"] = "disabled"
        button8["state"] = "disabled"
        button9["state"] = "disabled"


        dec = False
def change_to_dec():
    global x
    global dec
    if dec == False:
        splitet = re.split('([-+/*])', x)

        if splitet[0] == '':
            splitet.remove("")
        for i in range(len(splitet)):
            znaki = ["+", "-", "*", "/"]
            if all(z not in splitet[i] for z in znaki):
                splitet[i] = str(int(splitet[i],2))
        x = "".join(splitet)
        var.set(x)
        button2['bg'] = "white"
        button3['bg'] = "white"
        button4['bg'] = "white"
        button5['bg'] = "white"
        button6['bg'] = "white"
        button7['bg'] = "white"
        button8['bg'] = "white"
        button9['bg'] = "white"
        button2["state"] = "normal"
        button3["state"] = "normal"
        button4["state"] = "normal"
        button5["state"] = "normal"
        button6["state"] = "normal"
        button7["state"] = "normal"
        button8["state"] = "normal"
        button9["state"] = "normal"
        dec = True
def add_char(y):
    global x
    global start
    lastvar = x[-1]
    if lastvar == "-" and y == "-":
        start = False
        x = x[:-1] + '+'
    elif lastvar in ['+', '*', '/', '-']:
        start = False
        x = x[:-1] + y
    else:
        start = False
        x += y
    var.set(x)


def add(y):
    global x
    global start
    if start:
        x = y
        start = False
    else:
        x += y
    var.set(x)


def delet():
    global x
    global start
    start = True
    x = "0"
    var.set(str(x))


def calc():
    global x
    global start
    lastvar = x[-1]
    if lastvar in ['+', '*', '/', '-']:
        x = "0"
    else:
        try:
            if dec:
                x = str(int(eval(x)))
            else:
                splitet = re.split('([-+/*])', x)
                if splitet[0] == '':
                    splitet.remove("")
                for i in range(len(splitet)):
                    znaki = ["+","-","*","/"]
                    if all(z not in splitet[i] for z in znaki):
                        splitet[i] = str(int(splitet[i], 2))
                x = "".join(splitet)
                x = int(eval(x))
                if x<0:
                    x = "-"+bin(x)[3:]
                else:
                    x = bin(x)[2:]
        except ZeroDivisionError:
            x = "0"
    var.set(str(x))
    start = True


root = tk.Tk()
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(size=25)
root.option_add("*Font", defaultFont)
var = tk.StringVar()
e1 = tk.Label(root, width=20, textvariable=var, relief=RAISED, anchor=E,bg="white")
e1.grid(row=0, column=0, columnspan=4, sticky="NSEW")
var.set(x)
v = tk.IntVar()
tk.Radiobutton(root, text="bin", variable=v, command=change_to_bin,relief=RAISED,  value=1,bg="white").grid(row=1, column=0, sticky="NSEW",
                                                                                  columnspan=2)
tk.Radiobutton(root, text="dec", variable=v, command=change_to_dec,relief=RAISED,  value=0,bg="white").grid(row=1, column=2, sticky="NSEW",
                                                                                  columnspan=2)
button1 = tk.Button(root, text='1', command=lambda: add("1"),bg="white")
button1.grid(row=4, column=0, sticky="NSEW")
button2 = tk.Button(root, text='2', command=lambda: add("2"),bg="white")
button2.grid(row=4, column=1, sticky="NSEW")
button3 = tk.Button(root, text='3', command=lambda: add("3"),bg="white")
button3.grid(row=4, column=2, sticky="NSEW")
button4 = tk.Button(root, text='4', command=lambda: add("4"),bg="white")
button4.grid(row=3, column=0, sticky="NSEW")
button5 = tk.Button(root, text='5', command=lambda: add("5"),bg="white")
button5.grid(row=3, column=1, sticky="NSEW")
button6 = tk.Button(root, text='6', command=lambda: add("6"),bg="white")
button6.grid(row=3, column=2, sticky="NSEW")
button7 = tk.Button(root, text='7', command=lambda: add("7"),bg="white")
button7.grid(row=2, column=0, sticky="NSEW")
button8 = tk.Button(root, text='8', command=lambda: add("8"),bg="white")
button8.grid(row=2, column=1, sticky="NSEW")
button9 =tk.Button(root, text='9', command=lambda: add("9"),bg="white")
button9.grid(row=2, column=2, sticky="NSEW")
tk.Button(root, text='0', command=lambda: add("0"),bg="white").grid(row=5, column=1, sticky="NSEW")
tk.Button(root, text='C', command=lambda: delet(),bg="white").grid(row=5, column=0, sticky="NSEW")
tk.Button(root, text='+', command=lambda: add_char("+"),bg="white").grid(row=2, column=3, sticky="NSEW")
tk.Button(root, text='-', command=lambda: add_char("-"),bg="white").grid(row=3, column=3, sticky="NSEW")
tk.Button(root, text='*', command=lambda: add_char("*"),bg="white").grid(row=4, column=3, sticky="NSEW")
tk.Button(root, text='/', command=lambda: add_char("/"),bg="white").grid(row=5, column=3, sticky="NSEW")
tk.Button(root, text='=', command=lambda: calc(),bg="white").grid(row=5, column=2, sticky="NSEW")
root.mainloop()
