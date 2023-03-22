print("Ingresá tu nombre:  ")
nombre = input()
print("Ingresá la cantidad de viajeros:  ")
viajeros = int(input())
acompanantes = viajeros // 30
precio = 50000*(viajeros + acompanantes)
print("$" + str(precio))