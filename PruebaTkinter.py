from tkinter import*


root = Tk()

root.title("Ejemplo")
sandwich = IntVar()
pizza = IntVar()
icecream = IntVar()


def OpcComida():
    OpcEscogida = ""
    if(sandwich.get() == 1):
        OpcEscogida == "sandwich"
    if(pizza.get() == 1):
        OpcEscogida == "pizza"
    if(icecream.get() == 1):
        OpcComida == "icecream"

    textfinal.config(text=OpcEscogida)


#foto = PhotoImage(file="C:/Users/Madra/Desktop/Diseño y Desarrollo web/Ejercicios en Python/sandwich1.jpg")
#Label(root, image=foto).pack()
mframe = Frame(root).pack()
Label(mframe, text="Elige:", width=50).pack()


Checkbutton(mframe, text="sandwich", variable=sandwich,
            onvalue=1, offvalue=0, command=OpcComida).pack()
textfinal = Label(mframe)
Checkbutton(mframe, text="pizza", variable=pizza,
            onvalue=1, offvalue=0, command=OpcComida).pack()
textfinal = Label(mframe)
Checkbutton(mframe, text="icecream", variable=icecream,
            onvalue=1, offvalue=0, command=OpcComida).pack()
textfinal = Label(mframe)

textfinal.pack()

root.mainloop()
