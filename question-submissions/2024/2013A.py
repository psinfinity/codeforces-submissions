# https://codeforces.com/contest/2013/problem/A
from math import ceil
for _ in range(int(input())):
    zhan_fruit = int(input())
    xy = [int(x) for x in input().split()]

    print(ceil(zhan_fruit/min(xy)))
