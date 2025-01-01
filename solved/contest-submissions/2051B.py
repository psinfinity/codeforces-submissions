for _ in range(int(input())):
    n,a,b,c = map(int,input().split())
    val = n//(a+b+c)
    n%=(a+b+c)
    if n==0:
        print(3*val)
    elif n-a<=0:
        print(3*val+1)
    elif n-a-b<=0:
        print(3*val+2)
    else:
        print(3*val+3)
