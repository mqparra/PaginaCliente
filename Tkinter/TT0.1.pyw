from tkinter import Tk, Label, Button, Entry
from math import *
import tkinter.font as font


def sumar():
    if txt1.get() == '':
        dig1 = 0
        dig2 = eval(txt2.get())
    elif txt2.get() == '':
        dig2 = 0
        dig1 = eval(txt1.get())
    else:
        dig1 = eval(txt1.get())
        dig2 = eval(txt2.get())
    txt3.delete(0, 'end')
    txt3.insert(0, dig1 + dig2)


def reubicar():
    dig3 = eval(txt3.get())
    txt1.delete(0, 'end')
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')
    txt1.insert(0, dig3)


def cerrar():
    ventana.destroy()


ventana = Tk()
ventana.title("Calculadora Básica")  # Cambiar el nombre de la ventana
ventana.geometry("1000x600")  # Configurar tamaño
miFont = font.Font(family='Helvetica', size=20, weight='bold')

lbl1 = Label(ventana, text='Primer numero', bg='yellow')

lbl2 = Label(ventana, text='Segundo numero', bg='yellow')

lbl3 = Label(ventana, text='Resultado', bg='yellow')

txt1 = Entry(ventana, bg='pink')

txt2 = Entry(ventana, bg='pink')

txt3 = Entry(ventana, bg='pink')

bt2 = Button(ventana, text='Sumar [enter]', bg='green', fg='red', command=sumar)

bt3 = Button(ventana, text='Reubicar [ctr derecho]', bg='red', command=reubicar)
bt4 = Button(ventana, text='Cerrar [esc]', bg='red', command=cerrar)

for i in [lbl1, lbl2, lbl3, txt1, txt2, txt3, bt2, bt3, bt4]:
    i['font'] = miFont

# lbl1.place(relx=0.03,rely=0.04, relwidth= 0.23 , relheight= 0.1)
# lbl2.place(relx=0.03,rely=0.17, relwidth= 0.23 , relheight= 0.1)
# lbl3.place(relx=0.03,rely=0.3, relwidth= 0.23 , relheight= 0.1)

# txt1.place(relx=0.35,rely=0.04, relwidth= 0.23 , relheight= 0.1)
# txt2.place(relx=0.35,rely=0.17, relwidth= 0.23 , relheight= 0.1)
# txt3.place(relx=0.35,rely=0.3, relwidth= 0.23 , relheight= 0.1)

# bt2.place(relx=0.7,rely=0.17, relwidth= 0.23 , relheight= 0.1)
# bt3.place(relx=0.7,rely=0.3, relwidth= 0.23 , relheight= 0.1)

lbl1.grid(row=0, column=0, sticky='nsew')
lbl2.grid(row=1, column=0, sticky='nsew')
lbl3.grid(row=2, column=0, sticky='nsew')

txt1.grid(row=0, column=1, sticky='nsew')
txt2.grid(row=1, column=1, sticky='nsew')
txt3.grid(row=2, column=1, sticky='nsew')

bt2.grid(row=1, column=2, sticky='nsew')
bt3.grid(row=2, column=2, sticky='nsew')
bt4.grid(row=2, column=3, sticky='nsew')

ventana.bind("<Return>", lambda _: sumar())
ventana.bind("<Control_R>", lambda _: reubicar())
ventana.bind("<Escape>", lambda _: cerrar())

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=4)
ventana.columnconfigure(3, weight=4)

ventana.mainloop()
