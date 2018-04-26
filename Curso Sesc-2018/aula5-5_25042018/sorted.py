gato={'ingles': 'cat','espanhol': 'gato','frances': 'chat','alemao':'katze','italiano':'gatto'}
comES=[]
print('exercicio 1')
print(sorted(gato.items()))
print('exercicio 2')
print(sorted(gato.values(),reverse=True))
print('exercicio 3')
for final in gato:
	if final.endswith('es'):
		comES.append(final)
print('As palavras que terminam com ES são: {}'.format(comES)) 
print('exercicio 4')

for chave,valor in gatos.items():
	if not chave.endswith('es'):
		print(valor)