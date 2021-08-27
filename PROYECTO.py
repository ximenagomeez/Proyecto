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

"""
def sumar():

def restar():

def multiplicar():

def dividir():
"""

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
Label2=Label(window, text=" 2 ")
Label2.grid(column=2, row=2, padx=15, pady=15)


#LABEL3--------------------------------------
Label3=Label(window, text=" 3 ")
Label3.grid(column=3, row=2, padx=15, pady=15)


#LABEL4--------------------------------------
Label4=Label(window, text=" 4 ")
Label4.grid(column=4, row=2, padx=15, pady=15)


#NIVEL 3

#LABEL5--------------------------------------
Label5=Label(window, text=" 5 ")
Label5.grid(column=1, row=3, padx=15, pady=15)


#LABEL6--------------------------------------
Label6=Label(window, text=" 6 ")
Label6.grid(column=2, row=3, padx=15, pady=15)


#LABEL7--------------------------------------
Label7=Label(window, text=" 7 ")
Label7.grid(column=3, row=3, padx=15, pady=15)


#LABEL8--------------------------------------
Label8=Label(window, text=" 8 ")
Label8.grid(column=4, row=3, padx=15, pady=15)


#NIVEL 4

#LABEL9--------------------------------------
Label9=Label(window, text=" 9 ")
Label9.grid(column=1, row=4, padx=15, pady=15)


#LABEL00--------------------------------------
Label00=Label(window, text=" 0 ")
Label00.grid(column=2, row=4, padx=15, pady=15)


#LABEL7--------------------------------------
Labeldel=Label(window, text=" <- ")
Labeldel.grid(column=3, row=4, padx=15, pady=15)

#LABEL8--------------------------------------
Labelent=Label(window, text=" ENTER ")
Labelent.grid(column=4, row=4, padx=15, pady=15)

#NIVEL 5

#LABEL9--------------------------------------
Label9=Label(window, text=" + ")
Label9.grid(column=1, row=5, padx=15, pady=15)


#LABEL00--------------------------------------
Label00=Label(window, text=" - ")
Label00.grid(column=2, row=5, padx=15, pady=15)


#LABEL7--------------------------------------
Labeldel=Label(window, text=" x ")
Labeldel.grid(column=3, row=5, padx=15, pady=15)

#LABEL8--------------------------------------
Labelent=Label(window, text=" % ")
Labelent.grid(column=4, row=5, padx=15, pady=15)

window.mainloop()
