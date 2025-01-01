def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return None


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr_m = list(map(int, input().split()))  # list ai doesnt have ai
    not_known = set(range(1, n + 1)) - set(map(int, input().split()))

    if len(not_known) == 0:
        print('1' * m)
    elif len(not_known) > 1:
        print('0' * m)
    else:
        i = binary_search(arr_m,0,m-1,not_known.pop())
        if i is None:
            print('0'*m)
        else:
            print('0'*i+'1'+'0'*(m-i-1))