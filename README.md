# Proyecto calculadora básica


Este proyecto consiste en la creación de un programa que pueda calcular operaciones básicas. El objetivo es ser capaz de abrir el programa en una diferente pestaña
y que esta aplicación sea capaz de resolver operaciones básicas.

![Aquí la descripción de la imagen por si no carga](https://github.com/ximenagomeez/Proyecto/blob/main/New%20Note%2017.08.2021%20rxkHs.pdf)

"""
Proyecto Calculadora básica

1.Diseñar página
2.agregar botones
3.Input a operador
4.funciones básicas, sumar restar, multiplicar, dividir
5.posibles resultados
6. print resultados
7.loop

"""
#DISEÑO PÁGINA-----------------------------------------------------------
from tkinter import *
window=Tk()
window.title("CALCULADORA BÁSICA")
window.config(bg="pink")

#ACTIONCODE----------------------------------

#NIVEL 1

#LABEL0.1--------------------------------------
Label0=Label(window, text="              ")
Label0.grid(column=2, row=1, padx=15, pady=15)


#NIVEL 2

#LABEL1--------------------------------------
Label1=Label(window, text=" 1 ")
Label1.grid(column=1, row=2, padx=15, pady=15)

###3Button1=Button(command=action)

#LABEL2--------------------------------------
Label1=Label(window, text=" 2 ")
Label1.grid(column=2, row=2, padx=15, pady=15)

#LABEL3--------------------------------------
Label1=Label(window, text=" 3 ")
Label1.grid(column=3, row=2, padx=15, pady=15)

#LABEL4--------------------------------------
Label1=Label(window, text=" 4 ")
Label1.grid(column=4, row=2, padx=15, pady=15)

#NIVEL 3

#LABEL5--------------------------------------
Label1=Label(window, text=" 5 ")
Label1.grid(column=1, row=3, padx=15, pady=15)

#LABEL6--------------------------------------
Label1=Label(window, text=" 6 ")
Label1.grid(column=2, row=3, padx=15, pady=15)

#LABEL7--------------------------------------
Label1=Label(window, text=" 7 ")
Label1.grid(column=3, row=3, padx=15, pady=15)

#LABEL8--------------------------------------
Label1=Label(window, text=" 8 ")
Label1.grid(column=4, row=3, padx=15, pady=15)

#NIVEL 4

#LABEL9--------------------------------------
Label1=Label(window, text=" 9 ")
Label1.grid(column=1, row=4, padx=15, pady=15)

#LABEL00--------------------------------------
Label1=Label(window, text=" 0 ")
Label1.grid(column=2, row=4, padx=15, pady=15)

#LABEL7--------------------------------------
Label1=Label(window, text=" <- ")
Label1.grid(column=3, row=4, padx=15, pady=15)

#LABEL8--------------------------------------
Label1=Label(window, text=" ENTER ")
Label1.grid(column=4, row=4, padx=15, pady=15)


window.mainloop()

![Preview of the proyect]()
