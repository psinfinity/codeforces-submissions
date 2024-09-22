# 22 september 2024
# ps2006

def dearrange(x):
    if x == 1:
        return 0
    if x == 2:
        return 1

    else:
        return (x - 1) * (dearrange(x - 1) + dearrange(x - 2))


print(dearrange(int(input()))%1000000007)