def imc():
	peso = float(input('Qual o seu peso : '))
	altura = float(input('Qual a sua altura: '))
	imc = (peso/altura**2)
	print ('Seu IMC é : {:.2f}' .format(imc))
	if imc <=20:
		print('IMC bom! Abaixo do Peso')
	elif 21 <= imc <=24.9:
		print ('IMC médio ! Peso Normal')
	elif 25 <= imc <=29.9:
		print ('IMC médio ! Sobrepeso Cuidado!')
	else:
		print ('IMC ruim! Obesidade')
imc()


