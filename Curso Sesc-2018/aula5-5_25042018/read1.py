import csv   #leitura do arquivo pessoas.csv -- usando o PRINT(LINHA)
with open('pessoas.csv', newline='') as arquivo:
	reader = csv.DictReader(arquivo)
	for linha in reader:
		print(linha)
