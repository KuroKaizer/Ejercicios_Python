from tkinter import*
from tkinter import messagebox
import sqlite3


#-----------------Funciones-------------------#


def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute(
            '''CREATE TABLE DATOSUSUARIOS(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NOMBRE_USUARIO VARCHAR(50),
               APELLIDO_USUARIO VARCHAR(50), 
               PASSWORD VARCHAR(50),
               DIRRECION VARCHAR(50),
               COMENTARIO VARCHAR(100))''')

        messagebox.showinfo("BBDD", "BBDD creada con exito")

    except:
        messagebox.showwarning("Atencion!", "Atencion la BBDD ya existe")


def salirAplicacion():
    valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
    if valor == "yes":
        root.destroy()


def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPassword.set("")
    miDireccion.set("")
    textoComentario.delete(1.0, END)


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = miNombre.get(), miApellido.get(), miPassword.get(
    ), miDireccion.get(), textoComentario.get(1.0, END)
    # miCursor.execute(
    # "INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get() +
    # "','" + miApellido.get() +
    # "','" + miPassword.get() +
    # "','" + miDireccion.get() +
    # "','" + textoComentario.get("1.0", END) + "')")
    miCursor.execute(
        "INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", datos())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con exito")


def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miId.get())
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPassword.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])
    miConexion.commit()


def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
                     "', APELLIDO_USUARIO='" + miApellido.get() +
                     "', PASSWORD='" + miPassword.get() +
                     "', DIRECCION='" + miDireccion.get() +
                     "', COMENTARIOS='" + textoComentario.get(1.0, END) + "'WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con exito")


def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con exito")


root = Tk()
#-----------------Barra del Menu-----------------#
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-------------------Labels--------------------------#
miFrame = Frame(root)
miFrame.pack()

idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")

idNombre = Label(miFrame, text="Nombre:")
idNombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")

idApellido = Label(miFrame, text="Apellido:")
idApellido.grid(row=2, column=0, padx=10, pady=10, sticky="e")

idPass = Label(miFrame, text="Contraseña:")
idPass.grid(row=3, column=0, padx=10, pady=10, sticky="e")

idDireccion = Label(miFrame, text="Direccion:")
idDireccion.grid(row=4, column=0, padx=10, pady=10, sticky="e")

idComent = Label(miFrame, text="Comentario:")
idComent.grid(row=5, column=0, padx=10, pady=10, sticky="e")

#--------------------Campos-------------------------#
miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPassword = StringVar()
miDireccion = StringVar()

cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=miPassword)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(fg="red", show="?", justify="right")

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#----------------------Botones inferiores------------------#
botonesFrame = Frame(root)
botonesFrame.pack()

botonCrear = Button(botonesFrame, text="Crear", command=crear)
botonCrear.grid(row=0, column=0, padx=10, pady=10, sticky="e")

botonLeer = Button(botonesFrame, text="Leer", command=leer)
botonLeer.grid(row=0, column=1, padx=10, pady=10, sticky="e")

botonUpdate = Button(botonesFrame, text="Update", command=actualizar)
botonUpdate.grid(row=0, column=2, padx=10, pady=10, sticky="e")

botonBorrar = Button(botonesFrame, text="Borrar", command=eliminar)
botonBorrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")


root.mainloop()
