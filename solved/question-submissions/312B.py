a,b,c,d = map(int,input().split())

val = (a/b) / (1 - (1-a/b)*(1-c/d))
print(val)