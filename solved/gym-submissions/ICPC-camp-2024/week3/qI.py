import sys

def main():
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline().strip())
        x = sys.stdin.readline().strip()
        z,h=0,0
        for i in range(len(x),0,-1):
            if x[i-1] == '1' and z>0:
                h+=i
                z-=1
            else:
                z+=1
        sys.stdout.write(str(h)+'\n')
if __name__ == '__main__':
    main()