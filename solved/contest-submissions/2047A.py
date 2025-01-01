sq = tuple(x**2 for x in range(1,100,2))

for t in range(int(input())):
    piece_len = int(input())
    pieces = list(map(int,input().split()))

    total = 0
    counter=0
    while pieces:
        total+=pieces.pop(0)
        if total in sq:
            counter+=1
    print(counter)