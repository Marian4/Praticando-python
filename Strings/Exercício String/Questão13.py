import random

print("Bem vindo ao Jogo da palavra embaralhada!")

jogar = str(input("jogar? Sim/N�o."))

while jogar == 'Sim' or jogar == 'sim':

	a = 'otorrinolaringologista'

	b = 'paralelepipedo'

	c = 'caminh�o'
	d = 'filtro'

	e = 'facebook'

	f = 'banheiro'

	g = 'torta'

	h = 'chocolate'

	i = 'j�piter'

	j = 'segredo'

	k = 'guardanapo'

	lista = [a,b,c,d,e,f,g,h,i,j,k]

	lista2 = []

	palavra = random.choice(lista)

	for i in palavra:

		lista2.append(i)

	random.shuffle(lista2)

	for j in range(len(palavra)):

		print(lista2[j],end='')

	print()

	resposta = input("\nQual � a palavra?\n")

	if resposta == palavra:

		print("\nParab�ns, voc� acertou!!")

		jogar = str(input("\njogar novamente? Sim/N�o.\n"))

	else:

		print("\nQue pena, voc� errou.\n")

		print("A resposta certa era",palavra)

		jogar = str(input("\njogar novamente? Sim/N�o.\n"))

print("Programa encerrado.")
