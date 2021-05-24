from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo
from bson.objectid import ObjectId

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 10000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS = "Escuela"
MONGO_COLECCION = "alumnos"

cliente = pymongo.MongoClient(
    MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_BASEDATOS]
coleccion = baseDatos[MONGO_COLECCION]
ID_ALUMNO = " "


def mostrarDatos(nombre="", sexo="", calificacion=""):
    objetoBuscar = {}
    if len(nombre) != 0:
        objetoBuscar["Nombre"] = nombre
    if len(sexo) != 0:
        objetoBuscar["Sexo"] = sexo
    if len(calificacion) != 0:
        objetoBuscar["Calificacion"] = calificacion
    try:
        registers = tabla.get_children()
        for register in registers:
            tabla.delete(register)
        for documento in coleccion.find(objetoBuscar):
            tabla.insert(
                '', 0, text=documento["_id"], values=documento["Nombre"])
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido"+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a MongoDB"+errorConexion)


def crearRegistro():
    if bool(nombre.get()) != 0 and bool(calificacion.get()) != 0 and bool(sexo.get() != 0):
        try:
            documento = {"Nombre": nombre.get(), "Sexo": sexo.get(),
                         "Calificacion": calificacion.get()}
            coleccion.insert(documento)
            nombre.delete(0, END)
            sexo.delete(0, END)
            calificacion.delete(0, END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrarDatos()


def dobleClickTabla(event):
    global ID_ALUMNO
    ID_ALUMNO = tabla.item(tabla.selection())["text"]
    # print(ID_ALUMNO)
    documento = coleccion.find({"_id": ObjectId(ID_ALUMNO)})[0]
    # print(documento)
    nombre.delete(0, END)
    nombre.insert(0, documento["Nombre"])
    sexo.delete(0, END)
    sexo.insert(0, documento["Sexo"])
    calificacion.delete(0, END)
    calificacion.insert(0, documento["Calificacion"])
    registro["state"] = "disabled"
    editar["state"] = "normal"
    borrar["state"] = "normal"


def editarRegistro():
    global ID_ALUMNO
    if len(nombre.get()) != 0 and len(sexo.get()) != 0 and len(calificacion.get()) != 0:
        try:
            idBuscar = {"_id": ObjectId(ID_ALUMNO)}
            nuevosValores = {"Nombre": nombre.get(
            ), "Sexo": sexo.get(), "Calificacion": calificacion.get()}
            coleccion.update(idBuscar, nuevosValores)
            nombre.delete(0, END)
            sexo.delete(0, END)
            calificacion.delete(0, END)
        except pymongo.errors.ConnectionFailure as error:
            print("error")
    else:
        messagebox.showerror("No pueden quedar campos vacios")
    mostrarDatos()
    registro["state"] = "normal"
    editar["state"] = "disabled"
    borrar["state"] = "disabled"


def borrarRegistro():
    global ID_ALUMNO
    try:
        idBuscar = {"_id": ObjectId(ID_ALUMNO)}
        coleccion.delete_one(idBuscar)
        nombre.delete(0, END)
        sexo.delete(0, END)
        calificacion.delete(0, END)
    except pymongo.errors.ConnectionFailure as error:
        print("error")
    mostrarDatos()
    registro["state"] = "normal"
    editar["state"] = "disabled"
    borrar["state"] = "disabled"


def buscarAlumno():
    mostrarDatos(buscarNombre.get(), buscarSexo.get(),
                 buscarCalificacion.get())


ventana = Tk()
tabla = ttk.Treeview(ventana, columns=2)
tabla.grid(row=1, column=0, columnspan=2)
tabla.heading("#0", text="ID")
tabla.heading("#1", text="NOMBRE")
tabla.bind("<Double-Button-1>", dobleClickTabla)

# Nombre
Label(ventana, text="Nombre").grid(row=2, column=0)
nombre = Entry(ventana)
nombre.grid(row=2, column=1, sticky=W+E)
nombre.focus()
# Sexo
Label(ventana, text="Sexo").grid(row=3, column=0)
sexo = Entry(ventana)
sexo.grid(row=3, column=1, sticky=W+E)
# Calificacion
Label(ventana, text="Calificacion").grid(row=4, column=0)
calificacion = Entry(ventana)
calificacion.grid(row=4, column=1, sticky=W+E)
# Boton Registro
registro = Button(ventana, text="Registrar Alumno",
                  command=crearRegistro, bg="green", fg="white")
registro.grid(row=5, columnspan=2, sticky=W+E)
# Boton Editar
editar = Button(ventana, text="Editar Alumno",
                command=editarRegistro, bg="yellow")
editar.grid(row=6, columnspan=2, sticky=W+E)
editar["state"] = "disabled"
# Boton Borrar
borrar = Button(ventana, text="Borrar Alumno",
                command=borrarRegistro, bg="red", fg="white")
borrar.grid(row=7, columnspan=2, sticky=W+E)
borrar["state"] = "disabled"
# Buscar Nombre
Label(ventana, text="Buscar por nombre").grid(row=8, column=0)
buscarNombre = Entry(ventana)
buscarNombre.grid(row=8, column=1, sticky=W+E)
# Buscar Sexo
Label(ventana, text="Buscar por sexo").grid(row=9, column=0)
buscarSexo = Entry(ventana)
buscarSexo.grid(row=9, column=1, sticky=W+E)
# Buscar Calificacion
Label(ventana, text="Buscar por calificacion").grid(row=10, column=0)
buscarCalificacion = Entry(ventana)
buscarCalificacion.grid(row=10, column=1, sticky=W+E)
# Boton Buscar
buscar = Button(ventana, text="Buscar Alumno",
                command=buscarAlumno, bg="blue", fg="white")
buscar.grid(row=11, columnspan=2, sticky=W+E)

mostrarDatos()
ventana.mainloop()
