for _ in range(int(input())):
    num = input()
    if len(num)>=3 and num[:2] == '10' and int(num[2:])>=2 and len(str(int(num[2:])))==len(num[2:]):
        print('YES')
    else:
        print('NO')