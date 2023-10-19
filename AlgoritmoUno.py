"""
Realizar un programa que lea un número y determine si es un número primo 
Ivan Sierra 🦆

"""

numero = int(input("Ingrese un numero positivo: "))

if numero > 1 and numero / numero:
    print("Es un numero primo")
else:
    print("No es numero primo")    
    