def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplicacion(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operacion erronea"

while True: 
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break
	except ValueError:
		print("Los valores introducidos no son correctos. Intentelo de nuevo")

operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, divide): ")	

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplicacion":
	print(multiplicacion(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))

else:
	print("Operacion no completada")	

print("Operacion ejecutada. Continuacion de ejecion del programa ")						