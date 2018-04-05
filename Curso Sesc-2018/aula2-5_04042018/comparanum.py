#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:09:27 2018

@author: pi
"""

num=5
numero=int(input('Escolha um número de 1 a 10 : '))
if numero == num:
    print('YES" Você acertou .... parabéns')
elif numero<num:
    print('O número digitado é menor do que o número SURPRESA')
else: 
    print('O número digitado é maior do que o número SURPRESA')
    