Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> #Aula 2/5 - Curso SESC Consolação
>>> feira=['legumes','frutas','verduras','pastel','caldo de cana']
>>> feira.append('ovos')
>>> feira
['legumes', 'frutas', 'verduras', 'pastel', 'caldo de cana', 'ovos']
>>> #COmando POP : retira um item da lista de strings
>>> #lista.pop('item')
>>> feira.pop(3)
'pastel'
>>> feira
['legumes', 'frutas', 'verduras', 'caldo de cana', 'ovos']
>>> feira.pop(4)
'ovos'
>>> feira
['legumes', 'frutas', 'verduras', 'caldo de cana']
>>> #Marcadores de variável: servem para referenciar uma variável dentro de um print
>>> a=3.0112
>>> print('Resultado = {}' .format(int(a)))
Resultado = 3
>>> b=3.0112
>>> print('Resultado = {}' .format(b))
Resultado = 3.0112
>>> c=3.0112
>>> print('Resultado ={}' .format(c))
Resultado =3.0112
>>> c='3.0112'
>>> print('Resultado ={}' .format(c))
Resultado =3.0112
>>> d=3.0112
>>> print('Resultado ={:.2f}' . format(d))
Resultado =3.01
>>> print('Resultado ={:.3f}' . format(d))
Resultado =3.011
>>> #Comando DIR : lista os comandos válidos para a variável
>>> dir('feira')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> #Comando HELP : mostra o que o comando faz com a variável
>>> help('lucas'.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> #Comando Input : Passo para a entrada de dados pelo usuário
>>> #<variável> = input(<'Mensagem para o usuário entrar com o Dado'>)
>>> nome = input('Qual o seu nome? ')
Qual o seu nome? Lucas
>>> nome
'Lucas'
>>> idade = int(input('Quantos anos você tem? '))
Quantos anos você tem? 40
>>> idade
40
>>> altura = float(input('Qual a sua altura em metros? '))
Qual a sua altura em metros? 1.85
>>> altura
1.85
>>> #Condicionais no Python
>>> 
