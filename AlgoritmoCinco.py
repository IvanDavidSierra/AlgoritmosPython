"""
Dado un tiempo en segundos, determinar cuantos minutos hay y cuantos segundos restan 
para convertirse en un minuto más
Ivan Sierra 🦆

"""

segundos = int(input("Digite un tiempo en segundos (s): "))
print("Ha digitado",segundos,"s")

minutos = segundos / 60
print(segundos, "segundos en minutos (m) son:", minutos,"min")

if minutos == 60: 
    print("Hacen falta 60 segundos para que sea otro minuto")
else:
    segundosRestantes = 60 - (segundos % 60)
    print("Segundos restantes para convertirse en otro minuto: ",segundosRestantes,"s")








