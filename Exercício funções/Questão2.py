def imprimeAté(n):
	for i in range(n+1):
		print()
		for j in range(1,i+1):
 			print (j,end=' ')
n = eval(input("digite um número:"))
imprimeAté(n)