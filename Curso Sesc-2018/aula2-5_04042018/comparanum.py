num=5
numero=int(input('Escolha um número de 1 a 10: '))
if numero==num:
	print('YES! Você acertou ... parabéns!')
elif numero<num:
	print('O numero digitado é menor do que o número SURPRESA')
else:
	print('O numero digitado é maior do que o número SURPRESA')