#DISEÑO PÁGINA
from tkinter import *

window=Tk()
window.title("CALCULADORA BÁSICA")
window.config(bg="pink")

display= Entry(window)
display.grid(row=1, columnspan=6, sticky=W+E)
i=0

#ACTIONCODE
def num(n):
    global i
    display.insert(i, n)
    i+=1

def operador(op):
    global i
    len= len(op)
    display.insert(i, op)
    i+=operador()

def borrar():
    display.borrar(0,END)

"""def undo()"""


#BOTONES NUMÉRICOS
Button(window, text="1", command=lambda:num(1)).grid(row=2, column=0, sticky=W+E)
Button(window, text="2",command=lambda:num(2)).grid(row=2, column=1, sticky=W+E)
Button(window, text="3",command=lambda:num(3)).grid(row=2, column=2, sticky=W+E)

Button(window, text="4",command=lambda:num(4)).grid(row=3, column=0, sticky=W+E)
Button(window, text="5",command=lambda:num(5)).grid(row=3, column=1, sticky=W+E)
Button(window, text="6",command=lambda:num(6)).grid(row=3, column=2, sticky=W+E)

Button(window, text="7",command=lambda:num(7)).grid(row=4, column=0, sticky=W+E)
Button(window, text="8",command=lambda:num(8)).grid(row=4, column=1, sticky=W+E)
Button(window, text="9",command=lambda:num(9)).grid(row=4, column=2, sticky=W+E)

Button(window, text="0",command=lambda:num(0)).grid(row=5, column=1, sticky=W+E)

#BOTONES OPERACIONES
Button(window, text="AC", command=lambda:borrar()).grid(row=5, column=0, sticky=W+E)
Button(window, text="%",command=lambda:num(0)).grid(row=5, column=2, sticky=W+E)

Button(window, text="+",command=lambda:num("+")).grid(row=2, column=3, sticky=W+E)
Button(window, text="-",command=lambda:num("-")).grid(row=3, column=3, sticky=W+E)
Button(window, text="*",command=lambda:num("*")).grid(row=4, column=3, sticky=W+E)
Button(window, text="/",command=lambda:num("/")).grid(row=5, column=3, sticky=W+E)

Button(window, text="DEL").grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(window, text="**",command=lambda:num("**")).grid(row=3, column=4, sticky=W+E)
Button(window, text="^2",command=lambda:num("**2")).grid(row=3, column=5, sticky=W+E)
Button(window, text="^(",command=lambda:num("(")).grid(row=4, column=4, sticky=W+E)
Button(window, text=")",command=lambda:num(")")).grid(row=4, column=5, sticky=W+E)
Button(window, text="=").grid(row=5, column=4, sticky=W+E, columnspan=2)


window.mainloop()

