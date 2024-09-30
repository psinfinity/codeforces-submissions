import sys
def counter(a, b):
    if a>=b:
        if b==1:
            return a
        for i in range(30):
            if b**i <= a < b**(i + 1):
                return 1 + counter(a-(b**i), b)
    else:
        return a
for _ in range(int(sys.stdin.readline())):
    nk = [int(x) for x in sys.stdin.readline().split()]
    sys.stdout.write(str(counter(nk[0], nk[1]))+'\n')