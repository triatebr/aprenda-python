Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> #Aula 2/5 - Curso SESC Consolação 04/04/2018
>>> print('Aula 2/5')
Aula 2/5
>>> #Exercício slide 46
>>> animal='gatinho'
>>> animal=[0:6]
SyntaxError: invalid syntax
>>> animal[0:6]
'gatinh'
>>> animal[0:6]+'a'
'gatinha'
>>> #Exercício slide 45
>>> serie='Stranger Things'
>>> serie.upper()
'STRANGER THINGS'
>>> serie.capitalize()
'Stranger things'
>>> serie[::-1]
'sgnihT regnartS'
>>> #Tamanho da String : len(<string>)
>>> novaserie='Star Trek Discovery'
>>> len(novaserie)
19
>>> #Comando Find : <string que contém o texto>.find('string que procuro')
>>> #<string que contém o texto>,find('string que procuro',<posição a partir da qual quero procurar>)
>>> novaserie.find('k')
8
>>> abertura='Espaço: a fronteira final... audaciosamente indo onde ninguém jamais esteve.'
>>> len(abertura)
76
>>> abertura.fint('t')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    abertura.fint('t')
AttributeError: 'str' object has no attribute 'fint'
>>> abertura.find('t')
14
>>> abertura.find('a',13)
18
>>> abertura.find('!')
-1
>>> #Comando Replace : troca uma string por outra dentro de um texto, porém a troca não é definitiva
>>> #<variavel>.replace('string que quero mudar','nova string')
>>> spock='Fascinante, capitão Kirk'
>>> spock.replace('Fascinante','Incrível')
'Incrível, capitão Kirk'
>>> #Listas: permitem armazenar várias informações diferentes (números, strings, lógico) em uma mesma variável
>>> #<variável> = [info1,info2,info3]
>>> meubicho=['Gato',9,True]
>>> meubicho[0]
'Gato'
>>> meubichp[3]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    meubichp[3]
NameError: name 'meubichp' is not defined
>>> meubicho[3]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    meubicho[3]
IndexError: list index out of range
>>> meubichp[2]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    meubichp[2]
NameError: name 'meubichp' is not defined
>>> meubicho[2]
True
>>> meubicho[1]
9
>>> #Em listas devemos nos atentar que sempre começa com '0', 1 , 2 , 3 e assim por diante
>>> #Comando Append: acrescenta dados ao final de uma lista
>>> #<variável>append(<variável2>)
>>> nomedaserie=['Gotham','A', 'Dark']
>>> nomedaserie.append('Knight')
>>> nomedaserie
['Gotham', 'A', 'Dark', 'Knight']
>>> nomes=['Ana','Lucas','Marcus','Dani']
>>> nomes.append('Michelle')
>>> nomes
['Ana', 'Lucas', 'Marcus', 'Dani', 'Michelle']
>>> #Comando Join : gruda os elementos de uma sequencia de strings, usando um parametro fornecido
>>> #'<parametro fornecido>'.join(<nome da sequencia>)
>>> herois=['Flash','Arrow','Supergirl')
SyntaxError: invalid syntax
>>> herois=['Flash','Arrow','Supergirl']
>>> herois
['Flash', 'Arrow', 'Supergirl']
>>> ' e '.join(herois)
'Flash e Arrow e Supergirl'
>>> #Comando Split : separa uma string em pontos onde existam separadores de texto (espaço, tab, enter, '/' , =)
>>> #criando uma lista de strings
>>> #',string>'.split('<separador>')
>>> '1,2,3,4'.split(' e ')
['1,2,3,4']
>>> '1,2,3,4'.split(',')
['1', '2', '3', '4']
>>> #Tuplas: são similares as listas, mas imutáveis. Não podemos adicionar ou modificar nenhum de seus elementos.
>>> #consome menos espaço da memória
>>> #<variavel> = (info1,info2,info3)
>>> #<variavel> =  info1,info2,info3
>>> a=(3,5,8)
>>> a
(3, 5, 8)
>>> b=3,5,8
>>> b
(3, 5, 8)
>>> a==b
True
>>> type(b)
<class 'tuple'>
>>> a=(1,)
>>> a
(1,)
>>> type(a)
<class 'tuple'>
>>> b=(1)
>>> b
1
>>> type(b)
<class 'int'>
>>> #os exemplos acima parecem iguais mas são reconehcidos de forma diferente pelo Python
>>> #exercícios slide 61
>>> chaves='Eu prefiro morrer do que perder a vida.'
>>> #1) WUal o tamanho da string?
>>> len(chaves)
39
>>> #2) Verifique se começa com 'p'
>>> chaves.startswith('p')
False
>>> #3) Verifique se termina com '.'
>>> chaves.endswith('.')
True
>>> #4) Verifique a posição do caracter ','
>>> chaves.find(',')
-1
>>> #5) Troque o caracter '.' por '!'
>>> chaves.replace('.','!')
'Eu prefiro morrer do que perder a vida!'
>>> #6) Dada a lista mercado =['1kg de banana','12 ovos','1kg de farinha'], acrescente a string 'fermento em pó'
>>> mercado =['1kg de banana','12 ovos','1kg de farinha']
>>> mercado.append('fermento em pó')
>>> mercado
['1kg de banana', '12 ovos', '1kg de farinha', 'fermento em pó']
>>> 
