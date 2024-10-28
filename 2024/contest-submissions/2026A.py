for i in range(int(input())):
    x,y,k = list(map(int,input().split()))
    k = min(x,y)
    print(f'0 0 {k} {k}')
    print(f'0 {k} {k} 0')