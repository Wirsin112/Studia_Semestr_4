import tkinter as tk
from tkinter import font
from tkinter import messagebox
x = 0
def add(ent, y):
    global  x
    x += y
    ent.delete(0,'end')
    ent.insert(tk.END,str(x))
    
root = tk.Tk()
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(size = 25)
root.option_add("*Font", defaultFont)
e1 = tk.Entry(root)
add(e1, 0)
e1.grid(row=0,column=1,columnspan = 1)

tk.Button(root,text='1',command= lambda: add(e1,1)).grid(row=1,column=0)
tk.Button(root,text='2',command= lambda: add(e1,2)).grid(row=1,column=1)
root.mainloop()
