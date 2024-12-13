def solve(x):
    soln = 1
    while x>1:
        x = x/2 - 1
        soln+=1
    print(soln)


for tc in range(int(input())):
    solve(int(input()))