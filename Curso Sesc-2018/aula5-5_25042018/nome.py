import csv
dados=[] #criação de uma lista
peso=0 
while True:
	nome = input('Entre com o nome ou digite "0" : ')
	print(nome)
	if nome=='0':
		break
	else:
		peso = input('Qual a sua peso: ')
		print(peso)
		altura = input('Qual a sua altura: ')
		print(altura)
		dados.append({'nome':nome, 'peso':peso,'altura':altura})
print(dados)



with open('/home/eta/Documentos/cadastro.csv','w',newline='') as csvfile:
	colunas =['nome','peso','altura']
	writer = csv.DictWriter(csvfile, fieldnames=colunas)
	writer.writeheader()
	for item in dados:
		writer.writerow(item)
		