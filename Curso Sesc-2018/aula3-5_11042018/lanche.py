#Exercício do WHILE -- slide 78
#para wxwcutar faz-se necessário salvar com extensão '.py'
#entrar no diretório e executar o seguinte comando 'python3 lanche.py'
i=1
valor=0
lista=[]
carteira=100   #carteira com R$100,00
while i<=5:
	nums=float(input('Entre com o valor do lanche do dia {}: R$ '.format(i)))  #função de formatar o valor
	valor=valor+nums
	i=i+1 
	lista.append(nums)   #usando listas, e acrescentando valores

print('Maior Valor gasto: R$ {:.2f}'.format(max(lista)))        #printa maior valor
print('Menor Valor gasto: R$ {:.2f}'.format(min(lista)))        #printa menor valor
print('Valor gasto: R$ {:.2f}'.format(valor))                   #printa total
print('A média de gastos: R$ {:.2f}'.format(valor/i))           #printa média
print('Sobrou na carteira: R$ {:.2f}'.format(carteira-valor))   #printa o valor que sobrou
