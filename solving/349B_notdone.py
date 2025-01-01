v = int(input())
arr = list(map(int,input().split()))
mapper = {}
for i in range(1,10):
    mapper[arr[i-1]] = i

print(str(mapper[min(mapper)])*()  )

