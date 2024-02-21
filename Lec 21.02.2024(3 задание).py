a = int(input('загадай целое число и потом угадай'))
n = 10
while n > 0:
    print('###')
    n-=1
b = -43194184939
while b != a:
    b = int(input())
print("угадал")