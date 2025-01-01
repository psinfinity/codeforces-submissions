for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.append(0)
    max_val = 0
    for i in range(n):
        max_val = max(max_val,max_val+a[i]-b[i+1])

    print(max_val)