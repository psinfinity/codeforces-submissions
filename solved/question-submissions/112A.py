def solve():
    str1 = input().upper()
    str2 = input().upper()

    for i in range(len(str1)):
        if str1[i]<str2[i]:
            return -1
        if str1[i]>str2[i]:
            return 1
    return 0
print(solve())