import csv
with open('/home/eta/Documentos/arquivo.csv','w',newline='') as csvfile:
	colunas =['nome','peso','altura','profissão']
	writer = csv.DictWriter(csvfile, fieldnames=colunas)
	writer.writeheader()
	writer.writerow({'nome':'Annie','peso': 35.5,'altura':1.30,'profissão':'Analista',})
	writer.writerow({'nome':'Claire','peso': 39.5,'altura':1.35,'profissão':'Gerente',})