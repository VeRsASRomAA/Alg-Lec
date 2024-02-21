a = 0
b = 1
n = int(input()) - 2
print(a)
print(b)
while n > 0:
    n-=1
    b = a+b
    a = b-a
    print(b)