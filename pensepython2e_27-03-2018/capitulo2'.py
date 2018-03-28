Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> n=42
>>> print('n')
n
>>> print(n)
42
>>> 42=n
SyntaxError: can't assign to literal
>>> 32=t
SyntaxError: can't assign to literal
>>> x=5
>>> p=8
>>> print(x)
5
>>> print(p)
8
>>> x=y=1
>>> print(x)
1
>>> print(x*9)
9
>>> print(y)
1
>>> print(x+y+9)
11
>>> print(x+y+9);
11
>>> print(x+y+9).
SyntaxError: invalid syntax
>>> f=7;
>>> print(f);
7
>>> print(f).
SyntaxError: invalid syntax
>>> xy
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    xy
NameError: name 'xy' is not defined
>>> x*y
1
>>> p*f
56
>>> pf
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pf
NameError: name 'pf' is not defined
>>> xy
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    xy
NameError: name 'xy' is not defined
>>> print('Exercicios capitulo 2')
Exercicios capitulo 2
>>> 4^2
6
>>> 4**2
16
>>> 4/3
1.3333333333333333
>>> 4/3*(3,14*(5**3))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    4/3*(3,14*(5**3))
TypeError: can't multiply sequence by non-int of type 'float'
>>> (3,14*(5**3))
(3, 1750)
>>> (3,14*5**3)
(3, 1750)
>>> (3.14*5**3)
392.5
>>> 4/3*(3.14*5**3)
523.3333333333333
>>> 24.95*40%
SyntaxError: invalid syntax
>>> 24.95*.40
9.98
>>> 24.95-(24.95*.4)
14.969999999999999
>>> 24.95-9.98
14.969999999999999
>>> (24.95-(24.95*.4))+3+59*.75
62.22
>>> 59*.75
44.25
>>> 44.25+3
47.25
>>> 44.25+3+14.96
62.21
>>> (24.95-(24.95*.4))+3+59*.75
62.22
>>> 59*.75
44.25
>>> 
