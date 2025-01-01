for _ in range(int(input())):
    a = input()
    b = input()

    i=0
    k=0
    
    while i<min(len(a),len(b)):
        if a[i]==b[i]:
            i+=1
            k=1
        else:
            break
    
    print(len(a[i:])+len(b[i:]) + i + k)