import sys

for _ in range(int(sys.stdin.readline())):
    def my_func(a):
        return str(2*a - 1)
    sys.stdout.write(my_func(int(sys.stdin.readline())) + '\n')