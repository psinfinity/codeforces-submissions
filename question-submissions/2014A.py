# https://codeforces.com/problemset/problem/2014/A

import sys

for _ in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    pouch,counter = 0,0
    for i in [person for person in map(int,sys.stdin.readline().strip().split()) if person>=k or person == 0]:    
        if i!=0 or pouch == 0:
            pouch+=i
        else:
            pouch-=1
            counter+=1
    sys.stdout.write(str(counter) + '\n')