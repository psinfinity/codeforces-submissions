n,a,b = map(int,input().split())
if n > a+b:
    print(b+1)
elif a+b == n:
    print(b)
elif n < a+b:
    print(n-a)