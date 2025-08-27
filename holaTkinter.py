from tkinter import *
from tkinter import ttk

def saluda():
  name = nombre.get()
  print(name)
  et2 = ttk.Label(v,text="Hola "+name)
  et2.grid(column=0, row=3)

v = Tk()
v.geometry("400x200")

img = PhotoImage(file='saludo.png')
et3 = ttk.Label(v,image=img, anchor="center")

et1 = ttk.Label(v, text="Cual es tu nombre: ")
et1.grid(column=0, row=0)

nombre = ttk.Entry(v)
nombre.grid(column=2, row=0)

saludo = ttk.Button(v,text="Saluda", command=saluda)
saludo.grid(column=2, row=1)

v.mainloop()
