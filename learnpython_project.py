from openfile_class import Openfile

print("\nBienvenido al sistema de análisis de archivos.\n")
print("Opción 1: Archivo a minúsculas\nOpción 2: Archivo a mayúsculas")
print("Opción 3: Contador de palabras\nOpción 4: Detector de direcciones de correo")
opUsu = input("Ingrese el número de la opción escogida: ")
archivo = Openfile()

try:
    opUsu = int(opUsu)
except:
    print("\n>>> La opción ingresada no es válida.")
    exit()

if opUsu == 1:
    fileUsu = input("\nIngrese el nombre del archivo que desea modificar: ")
    print("\n")
    archivo.file_lowercase(fileUsu)

elif opUsu == 2:
    fileUsu = input("\nIngrese el nombre del archivo que desea modificar: ")
    print("\n")
    archivo.file_uppercase(fileUsu)

elif opUsu == 3:
    fileUsu = input("\nIngrese el nombre del archivo que desea analizar: ")
    print("\n")
    archivo.file_countwords(fileUsu)

elif opUsu == 4:
    fileUsu = input("\nIngrese el nombre del archivo que desea analizar: ")
    print("\n")
    archivo.file_mailsfinder(fileUsu)

else:
    print("\n>>> La opción ingresada no es válida")
    exit()
