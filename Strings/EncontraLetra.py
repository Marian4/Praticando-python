string = input("Digite uma frase/palavra:")
letra = input("Que letra deseja encontrar?")
for i in string:
	if i == letra:
		print("Letra encontrada")
		break
repetição = string.count(letra)
if repetição == 0:
        print("Letra não encontrada!")
elif repetição > 0:
        print("A letra se repete",repetição,"vezes na frase")

