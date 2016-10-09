string = input("Digite uma palavra/frase:")
string2 = string.replace(' ','')
print("\nPalavra/Frase:",string)
if not(string2.islower()):
	string2 = string2.lower()
if string2 == (string2[::-1]):
	print('\nEssa palavra/frase (ignorando os espaços) é um palíndromo.')
else:
	print('\nEssa palavra/frase (ignorando os espaços) não é um palíndromo.')
