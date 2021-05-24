from tkinter import *

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViajes():
	opcionEscogida=""
	if (playa.get()==1):
		opcionEscogida+="Playa"
	if (montagna.get()==1):
		opcionEscogida+="Montaña"
	if (turismoRural.get()==1):
		opcionEscogida+="Turismo Rural"

	textoFinal.config(text=opcionEscogida)			

foto=PhotoImage(file="Practica.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViajes).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()