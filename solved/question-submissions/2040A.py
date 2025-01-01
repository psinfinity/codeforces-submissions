def solve():

    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    # k
    for i in range(n):
        for j in range(n):
            if i!=j and abs(arr[i]-arr[j])%k == 0:
                break
            if j == n-1:
                print("YES")
                print(i+1)
                return True
    print("NO")
    return False

for _ in range(int(input())):
    solve()