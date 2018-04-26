import csv #cria o arquivo pessoas2.csv com 2 linhas
with open('/home/eta/Documentos/pessoas2.csv','w',newline='') as csvfile:
	colunas =['nome','peso','altura']
	writer = csv.DictWriter(csvfile, fieldnames=colunas)
	writer.writeheader()
	writer.writerow({'nome':'Patt','peso': 55.5,'altura':1.80,})
	writer.writerow({'nome':'Mary','peso': 29.5,'altura':1.25,})