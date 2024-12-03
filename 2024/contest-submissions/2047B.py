for t in range(int(input())):
    n = input()
    freq = {}
    given_str = input()
    for i in given_str:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1

    max_val = 0
    min_val = 12
    for i in freq.keys():
        if freq[i]>max_val:
            new_max = i
            max_val = freq[i]
        if freq[i]<=min_val:
            new_min = i
            min_val = freq[i]

    given_str = given_str.replace(new_min,new_max,1)
    print(given_str)