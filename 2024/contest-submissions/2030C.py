for _ in range(int(input())):
    strlen = int(input())
    arr = input()

    if arr[0]=='1' or arr[-1]=='1' or arr.count('11')>0:
        print("YES")

    else:
        print("NO")