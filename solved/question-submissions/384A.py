from math import ceil
n = int(input())
print(ceil(n*n/2))
if n%2==1:
    for i in range(1,n*n+1):
        if i%2==1:
            print('C',end="")
        else:
            print('.',end="")
        if i%n==0:
            print()
else:
    for i in range(1,n+1):
        if i%2==1:
            print("C."*int(n/2))
        else:
            print(".C"*int(n/2))
