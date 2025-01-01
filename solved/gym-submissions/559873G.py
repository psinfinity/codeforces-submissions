def solve():
    n = int(input())
    seats = list(map(int,input().split()))
    seat_dict = {i:False for i in range(1,n+1)}
    seat_dict[seats[0]]=True
    if seats[0]-1 in seat_dict:
        seat_dict[seats[0]-1]=True
    if seats[0]+1 in seat_dict:
        seat_dict[seats[0]+1]=True

    for seat in seats[1:]:
        if seat_dict[seat]:
            if seat - 1 in seat_dict:
                seat_dict[seat - 1] = True
            if seat + 1 in seat_dict:
                seat_dict[seat + 1] = True
        else:
            print('NO')
            return False
    print('YES')
    return True

for _ in range(int(input())):
    solve()