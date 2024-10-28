# https://codeforces.com/problemset/problem/2013/B
for _ in range(int(input())):
    n = int(input())
    f = [int(x) for x in input().split()]
    if n==1:
        print(f[0])
    else:
        print(sum(f) - 2*(f[-2]))