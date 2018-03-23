Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 7.0/2
3.5
>>> 7/2.
3.5
>>> print 2,4*2
SyntaxError: Missing parentheses in call to 'print'
>>> print 2.4*2
SyntaxError: Missing parentheses in call to 'print'
>>> 2.4
2.4
>>> 1 + 2 * 3
7
>>> print (2.4*2)
4.8
>>> 7+/2
SyntaxError: invalid syntax
>>> 1.5/0
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    1.5/0
ZeroDivisionError: float division by zero
>>> 9.85 * 1.686
16.6071
>>> 11.95 * 1.686
20.147699999999997
>>> d = 1.686
>>> 9.85*d
16.6071
>>> 11.95*d
20.147699999999997
>>> print 5*d , 7*d , 9*d
SyntaxError: Missing parentheses in call to 'print'
>>> print (5*d , 7*d , 9*d)
8.43 11.802 15.174
>>> >>> print (5*d , 7*d , 9*d)
SyntaxError: invalid syntax
>>>  print 5*d , 7*d , 9*d
 
SyntaxError: Missing parentheses in call to 'print'
>>> d=1.61
>>> print(4*d,5*d,6*d,7*d,9*d)
6.44 8.05 9.66 11.270000000000001 14.49
>>> lista=[5,6,7,8,9]
>>> for p in lista: print p*d
SyntaxError: Missing parentheses in call to 'print'
>>> for p in lista: print (p*d)
8.05
SyntaxError: invalid syntax
>>> for p in lista: print (p*d)

8.05
9.66
11.270000000000001
12.88
14.49
>>> range
<class 'range'>
>>> range(5)
range(0, 5)
>>> range(2,5)
range(2, 5)
>>> range(4,16)
range(4, 16)
>>> for p in range(4,16): print(p*d)

6.44
8.05
9.66
11.270000000000001
12.88
14.49
16.1
17.71
19.32
20.93
22.540000000000003
24.150000000000002
>>> for p in range(4,16): print (p) , print(p*d)

4
6.44
(None, None)
5
8.05
(None, None)
6
9.66
(None, None)
7
11.270000000000001
(None, None)
8
12.88
(None, None)
9
14.49
(None, None)
10
16.1
(None, None)
11
17.71
(None, None)
12
19.32
(None, None)
13
20.93
(None, None)
14
22.540000000000003
(None, None)
15
24.150000000000002
(None, None)
>>> for p in range(4,16): print (p) , (p*d)

4
(None, 6.44)
5
(None, 8.05)
6
(None, 9.66)
7
(None, 11.270000000000001)
8
(None, 12.88)
9
(None, 14.49)
10
(None, 16.1)
11
(None, 17.71)
12
(None, 19.32)
13
(None, 20.93)
14
(None, 22.540000000000003)
15
(None, 24.150000000000002)
>>> d=1.86
>>> for p in range(50,150): print(p).print(p*d)

50
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    for p in range(50,150): print(p).print(p*d)
AttributeError: 'NoneType' object has no attribute 'print'
>>> for p in range(50,150): print(p),print(p*d)

50
93.0
(None, None)
51
94.86
(None, None)
52
96.72
(None, None)
53
98.58
(None, None)
54
100.44000000000001
(None, None)
55
102.30000000000001
(None, None)
56
104.16000000000001
(None, None)
57
106.02000000000001
(None, None)
58
107.88000000000001
(None, None)
59
109.74000000000001
(None, None)
60
111.60000000000001
(None, None)
61
113.46000000000001
(None, None)
62
115.32000000000001
(None, None)
63
117.18
(None, None)
64
119.04
(None, None)
65
120.9
(None, None)
66
122.76
(None, None)
67
124.62
(None, None)
68
126.48
(None, None)
69
128.34
(None, None)
70
130.20000000000002
(None, None)
71
132.06
(None, None)
72
133.92000000000002
(None, None)
73
135.78
(None, None)
74
137.64000000000001
(None, None)
75
139.5
(None, None)
76
141.36
(None, None)
77
143.22
(None, None)
78
145.08
(None, None)
79
146.94
(None, None)
80
148.8
(None, None)
81
150.66
(None, None)
82
152.52
(None, None)
83
154.38
(None, None)
84
156.24
(None, None)
85
158.1
(None, None)
86
159.96
(None, None)
87
161.82000000000002
(None, None)
88
163.68
(None, None)
89
165.54000000000002
(None, None)
90
167.4
(None, None)
91
169.26000000000002
(None, None)
92
171.12
(None, None)
93
172.98000000000002
(None, None)
94
174.84
(None, None)
95
176.70000000000002
(None, None)
96
178.56
(None, None)
97
180.42000000000002
(None, None)
98
182.28
(None, None)
99
184.14000000000001
(None, None)
100
186.0
(None, None)
101
187.86
(None, None)
102
189.72
(None, None)
103
191.58
(None, None)
104
193.44
(None, None)
105
195.3
(None, None)
106
197.16
(None, None)
107
199.02
(None, None)
108
200.88000000000002
(None, None)
109
202.74
(None, None)
110
204.60000000000002
(None, None)
111
206.46
(None, None)
112
208.32000000000002
(None, None)
113
210.18
(None, None)
114
212.04000000000002
(None, None)
115
213.9
(None, None)
116
215.76000000000002
(None, None)
117
217.62
(None, None)
118
219.48000000000002
(None, None)
119
221.34
(None, None)
120
223.20000000000002
(None, None)
121
225.06
(None, None)
122
226.92000000000002
(None, None)
123
228.78
(None, None)
124
230.64000000000001
(None, None)
125
232.5
(None, None)
126
234.36
(None, None)
127
236.22
(None, None)
128
238.08
(None, None)
129
239.94000000000003
(None, None)
130
241.8
(None, None)
131
243.66000000000003
(None, None)
132
245.52
(None, None)
133
247.38000000000002
(None, None)
134
249.24
(None, None)
135
251.10000000000002
(None, None)
136
252.96
(None, None)
137
254.82000000000002
(None, None)
138
256.68
(None, None)
139
258.54
(None, None)
140
260.40000000000003
(None, None)
141
262.26
(None, None)
142
264.12
(None, None)
143
265.98
(None, None)
144
267.84000000000003
(None, None)
145
269.7
(None, None)
146
271.56
(None, None)
147
273.42
(None, None)
148
275.28000000000003
(None, None)
149
277.14
(None, None)
>>
