left = [0,0]
right = [0,0]
for i in range(int(input())):
    l,r = map(int,input().split())
    left[l]+=1
    right[r]+=1

print(min(left)+min(right))