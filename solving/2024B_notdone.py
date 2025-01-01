for _ in range(int(input())):
    n,k = map(int,input().split()) # n_slots, # req_cans
    arr = sorted(list(map(int,input().split())),key=reversed)
