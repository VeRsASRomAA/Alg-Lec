#1
# 1)
from math import sqrt,sin,exp,pi 
x=int(input("Введите число x: "))
if x < 0:
    print("(1)",4)
if 0 <=x<1:
    print(x**2+3*x+4)
if x > 1:
    print(x+7)
# 2)
a=int(input("Введите число a: "))
b=int(input("Введите число b: "))
x=int(input("Введите число x: "))
if x < 0:
    print(sin(x+(pi/2))**2)
if a<=x<=b:
    print((exp**2)*sin(x+(pi/2)))
if x > b:
    print(sqrt(abs(sin(x+(pi/3))+2.1*(10**-3))))