from math import sqrt

def solve(n):
    counter=0
    for c in range(5,n+1):
        for a in range(1,int(c/(2**0.5))+1):
            b2 = c**2 - a**2
            if int(sqrt(b2)) == sqrt(b2):
                counter+=1
    print(counter)
    return 0

solve(int(input()))