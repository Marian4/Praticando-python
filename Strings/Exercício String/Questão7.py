frase = input("digite uma frase:")
espa�os = frase.count(' ')
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')
vogais = a + e + i + o + u
print("\nH� %i espa�os em branco na frase e %i vogais:\n\na -> %i\ne -> %i\ni -> %i\no -> %i\nu -> %i"%(espa�os,vogais,a,e,i,o,u))
