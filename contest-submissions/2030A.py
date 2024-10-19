for _ in range(int(input())):
    arr_len = int(input())
    arr = [int(i) for i in input().split()]
    print((max(arr)-min(arr))*(arr_len-1))