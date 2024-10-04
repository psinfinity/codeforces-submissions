# https://codeforces.com/problemset/problem/2008/A
for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    if a&1 or (a==0 and b&1):
        print("NO")
    else:
        print("YES")