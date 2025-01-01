n,m = map(int,input().split())
arr = list(map(int,input().split()))

already = {}
mapper = {}
count=0
for i in range(n-1,-1,-1):
    if arr[i] not in already:
        already[arr[i]] = True
        count+=1
    mapper[i]=count


for _ in range(m):
    x = int(input())
    print(mapper[x-1])