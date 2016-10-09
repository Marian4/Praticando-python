string1 = str(input("esreva uma frase:"))
string2 = str(input("esreva outra frase:"))
print("\nFrase 1: %s\nTamanho: %i caracteres\n"%(string1,len(string1)))
print("Frase 2: %s\nTamanho: %i caracteres\n"%(string2,len(string2)))
if len(string1) == len(string2):
	print("As duas frases tem o mesmo tamanho",end=' ')
else:
	print("As duas frases tem tamanhos diferentes",end=' ')
if string1 == string2:
	print("e possuem o mesmo conteúdo.")
else:
	print("e possuem conteúdos diferentes.")