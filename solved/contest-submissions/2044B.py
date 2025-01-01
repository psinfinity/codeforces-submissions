for _ in range(int(input())):
    my_str = input()[::-1]
    for i in my_str:
        if i=='p':
            print('q',end="")
        elif i=='q':
            print('p',end="")
        else:
            print('w',end="")
    print()