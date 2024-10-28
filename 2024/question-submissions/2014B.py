# https://codeforces.com/problemset/problem/2014/B

import sys

for _ in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    if (n&1==0 and (k%4 in (0,1))) or (n&1 and (k%4 in (0,3))):
        sys.stdout.write('YES' + '\n')
    else:
        sys.stdout.write('NO' + '\n')