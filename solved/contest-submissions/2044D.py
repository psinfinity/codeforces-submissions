import sys
for _ in range(int(input())):
    arr_len = int(input())
    arr = list(map(int,input().split()))
    done = set()
    i=1
    max_val = 0
    for num in arr:
        if num in done:
            while i in done:
                i+=1
            done.add(i)
            sys.stdout.write(str(i)+" ")
        else:
            done.add(num)
            sys.stdout.write(str(num)+" ")

    sys.stdout.write('\n')