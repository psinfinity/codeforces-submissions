k = int(input())
mapper = {}
for _ in range(4):
    for char in input():
        if char == '.':
            continue
        if char not in mapper:
            mapper[char] = 1
        else:
            mapper[char] += 1
if [True for char in mapper.values() if char > 2*k]:
    print('NO')
else:
    print('YES')