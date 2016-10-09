def AM(horas,minutos):
	if horas > 12:
		horas -= 12
		minutos = minutos
	else:
		horas = horas
		minutos = minutos
	return horas,minutos
hora = eval(input("hora:"))
minuto = eval(input("minuto:"))
h,m = AM(hora,minuto)
print("Conversão\n P.M - %i:%i\n A.M - %i:%i "%(hora,minuto,h,m))