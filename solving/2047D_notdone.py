for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    solved_arr = sorted(arr)
    i = 0
    while i < n:
        if arr[i]!=solved_arr[i]:
            break
        i+=1

    if arr[-1] <= arr[i]+1:
        solved_arr = solved_arr[:i+1] + [num+1 for num in solved_arr[i+1:]]
    else:
        solved_arr = solved_arr[:i+2] + [num + 1 for num in solved_arr[i+2:]]


    for item in solved_arr:
        print(item,end=" ")
    print()