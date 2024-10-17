from math import ceil

a,b = [int(x) for x in input().split()]
n = (a*b)/10
for i in range(1,10):
    print(int(ceil(i*n)),end=" ")