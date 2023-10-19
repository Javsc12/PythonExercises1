filename = input("Ingresa el nombre del archivo con extension: ")

filename_split = filename.split(".")

print(filename_split[-1])
print ("La extension del archivo es : " + repr(filename_split[-1])) ## La función repr() devuelve una cadena que contiene una representación imprimible de un objeto.