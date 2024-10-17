for _ in range(int(input())):
    card_no, max_distinct = list(map(int,input().split()))
    cards = sorted(list(map(int,input().split())))
    ans = 0
    j=0
    for i in range(card_no):
        j = max(i,j)
        while j+1<card_no and cards[1+j]-cards[j]<=1 and cards[1+j]-cards[i] < max_distinct:
            j+=1
        ans = max(ans, j-i+1)

    print(ans)