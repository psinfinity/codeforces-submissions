for _ in range(int(input())):
    a,b = map(int,input().split())
    x = b-a
    if x<=0:
        print(a)
    else:
        if (a-x)<0:
            print(0)
        else:
            print(a-x)