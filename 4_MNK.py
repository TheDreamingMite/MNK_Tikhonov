# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 

@author: Владимир
"""

import numpy as np

import matplotlib.pyplot as plt
plt.xlabel('coordinate axis X')
plt.ylabel('axis Y')
#x = np.array([0, 2, 3, 4, 5])
#y = np.array([2, 34, 67, 79, 89])
fp = open('MNK.txt','r')  # открыть файл из любого каталога
a=fp.readline()
k=-1
x = np.array([0]*100)
y = np.array([0]*100)
while a!='':
    k=k+1
    n = a.find(' ')
    x[k]=int(a[:n])
    y[k]=int(a[n:])
    a=fp.readline()
for i in range(k):
    print(x[i], "  ",y[i])
n1 = len(x)
n2 = len(y)
n=0
if(n1!=n2):
    print("Ваши данные неправильно введены")
else:
    n=n1
sx = 0;
sy = 0;
for i in range(n):
    sx = sx + x[i]
for i in range(n):
    sy = sy + y[i]
sxx = 0;
for i in range(n):
    sxx = sxx + x[i]*x[i]
sxy = 0;
for i in range(n):
    sxy = sxy + y[i]*x[i]
syy = 0;
for i in range(n):
    syy = syy + y[i]*y[i]

A = (sy*sxx - sx*sxy) / (n * sxx - sx * sx)
B = (n * sxy - sx * sy) / (n * sxx - sx * sx)
plt.grid()
min0 = x.min()
max0 = x.max()
x0 = np.array([min0,max0])
y0 = np.array([min0*B + A,max0*B + A])

plt.scatter(x, y)
plt.plot(x0, y0, color = 'red')
"""plt.errorbar(x, y, xerr=0.2, yerr=5)"""
plt.errorbar(x, y, xerr=0.2, yerr=5, fmt='none', ecolor='blue')
plt.title("Simplest MNK chart's")
plt.show()


""" Погрешности коэффициентов """
ky = 0;
for i in range(n):
    ky = ky + (y[i] - A - B*x[i]) * (y[i] - A - B*x[i])
ky = ky/(n-2)
SA = (ky*sxx/(n*sxx - sx*sx))**0.5
SB = (ky*n/(n*sxx - sx*sx))**0.5

print('y = bx + a')
print( 'a = ', A)
print( 'Sa = ', SA)
print( 'b = ', B)
print('Sb = ', SB)
