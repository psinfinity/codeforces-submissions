import sys

n = int(sys.stdin.readline()[:-1])
abel = int(sys.stdin.readline()[:-1])


def main_func():
    for _ in range(n-1):
        if int(sys.stdin.readline()[:-1]) > abel:
            return 'N'

    return 'S'


print(main_func())