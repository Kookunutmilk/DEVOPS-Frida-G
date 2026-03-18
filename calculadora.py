#Calculadora 17/09/2024
#Fri G

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def exponenciacion(a, b):
    return a ** b

print("Calculadora Simple")
print("Opciones:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Exponenciación")
opcion = input("Escribe el número de la operación que deseas realizar: ")

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

if opcion == "1":
    print("Resultado:", suma(a, b))
elif opcion == "2":
    print("Resultado:", resta(a, b))
elif opcion == "3":
    print("Resultado:", multiplicacion(a, b))
elif opcion == "4":
    print("Resultado:", exponenciacion(a, b))

else:
    print("Opción no válida")