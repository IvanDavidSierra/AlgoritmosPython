""""
Dado dos numeros enteros, donde estos numeros formaran un intervalo, 
es decir el primer numero debe ser menor que el segundo (se debe ejecutar 
hasta que sea valido el intervalo), y se deben sumar los numeros del intervalo

Ivan Sierra 🦆

"""

numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))
banderaUno = True 

while banderaUno:
    if numeroUno < numeroDos:
        banderaUno = False
        print("El intervalo de numero es: [",numeroUno,",",numeroDos,"]")
        sumaNumeros = numeroUno + numeroDos
        print("La suma del intervalo es:",sumaNumeros)
    else:
        print("Para que el intervalo sea valido, el primer numero debe ser menor al segundo")
        banderaUno

        