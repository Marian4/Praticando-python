custo = eval(input("qual o custo do item(R$)?"))
taxaImposto = eval(input("qual a taxa do imposto(%)?"))
def somaImposto(custo,taxaImposto):
	custoTotal = custo +((custo/100)*taxaImposto)
	return custoTotal
print("o custo total é de R$%.2f"%somaImposto(custo,taxaImposto))