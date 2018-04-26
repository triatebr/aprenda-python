import csv   #leitura do arquivo pessoas.csv
with open('pessoas.csv', newline='') as arquivo:
	reader = csv.DictReader(arquivo)
	for linha in reader:
		print('Nome: '+linha['nome'], 'Peso: '+linha['peso'],'Altura: '+linha['altura'])
		#print(linha['peso'],linha['altura'],linha['nome'])