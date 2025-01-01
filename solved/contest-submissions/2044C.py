for _ in range(int(input())):
    m,a,b,c = map(int,input().split())
    left = 2*m - min(m,a) - min(m,b)
    if left > c:
        print(2*m - left + c)
    else:
        print(2*m)