lista=['Java','JavaScript','PHP','C','Python','Pascal','Press']
comP=[]
for linguagem in lista:
	if linguagem.startswith('P'):
		comP.append(linguagem)  #usando listas para agrupar as linguagens que se iniciam com 'P'
comecaP=' , '.join(comP)        #usa-se o Join para tratar a lista e usar/printar como string
print('A linguagem de Programação que começam com "P" é : {} ' .format(comecaP))
		
#diferenças entre o WHILE e o FOR
