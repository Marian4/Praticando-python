print("informe sua data de nascimento.\n")
dia = eval(input("dia:"))
mes = eval(input("mês:"))
ano = eval(input("ano:"))
print("\nData de nascimento:%i/%i/%i\n"%(dia,mes,ano))
extenso = ''
if mes == 1:
	extenso = 'Janeiro'
elif mes == 2:
	extenso = 'Fevereiro'
elif mes == 3:
	extenso = 'Março'
elif mes == 4:
	extenso = 'Abril'
elif mes == 5:
	extenso = 'Maio'
elif mes == 6:
	extenso = 'Junho'
elif mes == 7:
	extenso = 'Julho'
elif mes == 8:
	extenso = 'Agosto'
elif mes == 9:
	extenso = 'Setembro'
elif mes == 10:
	extenso = 'Outubro'
elif mes == 11:
	extenso = 'Novembro'
else:
	extenso = 'Dezembro'
print("Você nasceu no dia %i de %s de %i."%(dia,extenso,ano))