# https://codeforces.com/contest/2005/problem/A

t = int(input())

test_cases = int(input())
mystring = ('aeiou')

for i in range(test_cases):

    length = int(input())
    values_list = [length // 5, length // 5, length // 5, length // 5, length // 5]
    ans = ''
    for j in range(length % 5):
        values_list[j] += 1
        length -= 1

    print(values_list[0] * 'a' + values_list[1] * 'e' + values_list[2] * 'i' + values_list[3] * 'o' + values_list[
        4] * 'u')