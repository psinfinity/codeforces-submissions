def solve():
    n,k = map(int,input().split())
    fruits = list(map(int,input().split()))
    heights = list(map(int,input().split()))
    possible = {}
    length = 0
    for i in range(n-1):
        if heights[i]%heights[i+1]==0:
            if i-length in possible:
                possible[i-length]+=1
                length+=1
            else:
                length=1
                possible[i]=2
    min_len = 0
    if fruits[-1]<=k:
        min_len=1

    for key in possible.keys():
        our_fruits = 0
        j=0
        for i in range(possible[key]):
            our_fruits+=fruits[key+i]
            if our_fruits>k:
                our_fruits-=fruits[key+j]
                j+=1
            min_len = max(min_len,i-j+1)
    if n==1 and fruits[0]<=k:
        min_len = 1

    print(min_len)

for _ in range(int(input())):
    solve()