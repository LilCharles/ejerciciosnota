lista = []
n = int(input("ingrese el largo de la lista: "))
while n < 1:
	n = int(input("ingrese el largo de la lista: "))

for i in range(2, n*2, 2):
	numero = i**3
	lista.append(int(numero))
