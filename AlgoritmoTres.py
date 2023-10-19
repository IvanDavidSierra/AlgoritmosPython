"""
Realiza un programa que determina la cantidad de numeros pares e impares entre 1 y 100, 
la suma de esa cantidad de numeros pares y suma de numeros impares
Ivan Sierra 🦆

"""

numerosPares = 0
numerosImpares = 0
i = 0


while (i<100):
    if i % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1    
    i+=1

sumaNumeros = numerosPares + numerosImpares
print(f"Hay un total de {numerosPares} numeros pares")
print(f"Hay {numerosImpares} numeros impares")
print(f"La suma de ambos datos es: {sumaNumeros}")