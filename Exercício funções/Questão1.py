def imprimeAté(n):
	for i in range(n+1):
		print()
		for j in range(i):
 			print (i,end=' ')
n = eval(input("digite um número:"))
imprimeAté(n)