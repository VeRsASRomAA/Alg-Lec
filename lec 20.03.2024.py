#coding utf:8
#1
a=[0,1]
n=int(input())
for i in range(2,n+1):
    f=a[i-2]+a[i-1]
    a.append(f)
print(a)
#2
a=[1,2,3,4,5,6,7,8,9,10,12,15,16,17]
b=[]
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)
#3
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,19,51,61,71]
b=[]
c=[]
for i in a:
    if i % 2 ==0:
        b.append(i)
    else:
        c.append(i)
print(b,c)
#4
a=[1,2,3,4,5,6,7,8,9,10,21,31,41,51,61]
b=a
for i in a:
    if i % 3 == 0:
        a.append(i)
print(a)
#5
a=(int(input()))
b=(int(input()))
c=(int(input()))
d=[]
for i in range(a,b,c):
    d.append(i)
print(sorted(d,reverse=True))
    