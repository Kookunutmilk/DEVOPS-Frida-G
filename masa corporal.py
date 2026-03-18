peso = int(input("Agregar peso: "))
altura = float(input("Agregar altura: "))

imc = round(peso / (altura ** 2), 2)

print("El índice de masa corporal es:", imc)
