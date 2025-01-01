from bisect import bisect_right, bisect

for _ in range(int(input())):
    n,x = map(int,input().split())
    corals = sorted(list(map(int,input().split())))

    h=x//n
    pt1 = bisect_right(corals,h)
    underwater_coral = sum(corals[:pt1])
    pt2=None
    h = (x + underwater_coral) // (pt1+1)
    old_h = 0

    while pt1!=pt2:
        h = (x + underwater_coral) // (pt1+1)
        if pt2 is not None:
            pt1=pt2
        pt2 = bisect_right(corals,h)
        underwater_coral+=sum(corals[pt1:pt2])
        old_h = h

    print(h)