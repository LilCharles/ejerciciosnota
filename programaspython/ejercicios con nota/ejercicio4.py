lista = []
n = int(input("ingrese el largo de la lista: "))
while n < 1:
	n = int(input("ingrese el largo de la lista: "))
for i in range(0, n):
	x = input("ingrese nombre: ")
	while x.lower() in lista or x.lower() == "admin":
		x = input("ingrese nombre: ")

	lista.append(x)
print(lista)
