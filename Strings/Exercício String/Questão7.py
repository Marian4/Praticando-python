frase = input("digite uma frase:")
espaços = frase.count(' ')
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')
vogais = a + e + i + o + u
print("\nHá %i espaços em branco na frase e %i vogais:\n\na -> %i\ne -> %i\ni -> %i\no -> %i\nu -> %i"%(espaços,vogais,a,e,i,o,u))
