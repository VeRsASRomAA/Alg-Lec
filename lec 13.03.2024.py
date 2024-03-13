import math
i=1
e=math.pow(10,-4)
while abs (((2*i)**2)/((2*i-1))-1)>e:
    i+=1
    x=((2*i)**2)/((2*i-1)*(2*i+1))
    print(x)
