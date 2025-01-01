def solve(str1, str2):
    map_val1 = {}
    map_val2 = {}
    for i in range(1,len(str1)):
        if str1[i] not in map_val1:
            map_val1[str1[i]] = i

    for i in range(len(str2)-1):
        map_val2[str2[i]] = i

    strings = [str1[:map_val1[key]] + str2[map_val2[key]:] for key in map_val1.keys() if key in map_val2]
    strings.sort(key=len)
    if not strings:
        return -1
    else:
        return strings[0]
if __name__ == "__main__":
    print(solve(input(),input()))