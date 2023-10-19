numbers = input("Ingresa los numeros separados por comas: ")

lista = numbers.split(",") ## (split) Divide una cadena en una lista donde cada palabra sea un elemento de la lista
tupla = tuple(lista)

print("Tupla: ", tupla)
print("Lista: ", lista)
