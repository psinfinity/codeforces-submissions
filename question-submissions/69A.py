sum_i,sum_j,sum_k=0,0,0

for i in range(int(input())):
    a,b,c=map(int,input().split())
    sum_i+=a
    sum_j+=b
    sum_k+=c

if sum_i==0 and sum_j==0 and sum_k==0:
    print("YES")
else:
    print("NO")