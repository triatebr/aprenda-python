Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> eu='Lucas'
>>> eu
'Lucas'
>>> d=1.902
>>> type(eu)
<class 'str'>
>>> type(d)
<class 'float'>
>>> type(1)
<class 'int'>
>>> type(1.)
<class 'float'>
>>> type(1,2,3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(1,2,3)
TypeError: type() argument 1 must be str, not int
>>> type([1,2,3])
<class 'list'>
>>> type(range)
<class 'type'>
>>> type(range(3))
<class 'range'>
>>> n1=10
>>> n2=20
>>> n1+n2
30
>>> n1='abacate'
>>> n2='banana'
>>> n1+n2
'abacatebanana'
>>> n2+n1
'bananaabacate'
>>> x=3.
>>> x*5
15.0
>>> 'x'*5
'xxxxx'
>>> [1,2] + [3,4]
[1, 2, 3, 4]
>>> '12' * 3
'121212'
>>> [1,2]*3
[1, 2, 1, 2, 1, 2]
>>> msg = 'um dólar vale %f real.'
>>> msg
'um dólar vale %f real.'
>>> print msg
SyntaxError: Missing parentheses in call to 'print'
>>> print(msg)
um dólar vale %f real.
>>> d=1.902
>>> print(msg % d)
um dólar vale 1.902000 real.
>>> msg2='Um dólar vale %f real e um real vale %f dólar.'
>>> print (msg2)
Um dólar vale %f real e um real vale %f dólar.
>>> print (msg2 % (d,1/d)))
SyntaxError: invalid syntax
>>> print (msg2 % (d,1/d))
Um dólar vale 1.902000 real e um real vale 0.525762 dólar.
>>> print (msg2 %.2 (d,1/d))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print (msg2 %.2 (d,1/d))
TypeError: 'float' object is not callable
>>> print (msg2 %.2f (d,1/d))
SyntaxError: invalid syntax
>>> d=1.685
>>> print('%.2f' d)
SyntaxError: invalid syntax
>>> '%.2f' %d
'1.69'
>>> 
print (msg2 %.2 (d,1/d))
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    print (msg2 %.2 (d,1/d))
TypeError: 'float' object is not callable
>>> print (msg2 %.2f (d,1/d))
SyntaxError: invalid syntax
>>> for p in range(4,16): print('US$ %.2F = R$ %.2F' % (P,P*D))

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for p in range(4,16): print('US$ %.2F = R$ %.2F' % (P,P*D))
NameError: name 'P' is not defined
>>> for p in range(4,16): print('US$ %.2F = R$ %.2F' % (p,p*d))

US$ 4.00 = R$ 6.74
US$ 5.00 = R$ 8.43
US$ 6.00 = R$ 10.11
US$ 7.00 = R$ 11.79
US$ 8.00 = R$ 13.48
US$ 9.00 = R$ 15.17
US$ 10.00 = R$ 16.85
US$ 11.00 = R$ 18.54
US$ 12.00 = R$ 20.22
US$ 13.00 = R$ 21.91
US$ 14.00 = R$ 23.59
US$ 15.00 = R$ 25.28

>>> for p in range(4,16): print('US$ %5.2F = R$ %5.2F' % (p,p*d))

US$  4.00 = R$  6.74
US$  5.00 = R$  8.43
US$  6.00 = R$ 10.11
US$  7.00 = R$ 11.79
US$  8.00 = R$ 13.48
US$  9.00 = R$ 15.17
US$ 10.00 = R$ 16.85
US$ 11.00 = R$ 18.54
US$ 12.00 = R$ 20.22
US$ 13.00 = R$ 21.91
US$ 14.00 = R$ 23.59
US$ 15.00 = R$ 25.28
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	v=i*3
	print(v)

	
0
3
6
9
12
>>> for i in range(12):
	v=i*7
	print(v)

	
0
7
14
21
28
35
42
49
56
63
70
77
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for p in range(9,13): print('US$ %5.2F = R$ %5.2F' %p, p*d)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    for p in range(9,13): print('US$ %5.2F = R$ %5.2F' %p, p*d)
TypeError: not enough arguments for format string
>>> for p in range(9,13): print('US$ %5.2F = R$ %5.2F' %(p, p*d))

US$  9.00 = R$ 15.17
US$ 10.00 = R$ 16.85
US$ 11.00 = R$ 18.54
US$ 12.00 = R$ 20.22
>>> 6%3
0
>>> 7%3
1
>>> 8%3
2
>>> 9%3
0
>>> 
