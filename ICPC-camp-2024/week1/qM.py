necklace = [0 if bead == 'A' else 1 for bead in input().strip()]
necksum = sum(necklace)


def checker():
    if necksum % 2 != 0 or len(necklace) % 2 != 0:
        print('NO')
        return False
    i = 0
    while i < int(len(necklace) / 2 + 1):
        i += abs(int(necksum / 2 - sum(necklace[i:int(i + len(necklace) / 2)])))

        if sum(necklace[i:int(i + len(necklace) / 2)]) == necksum / 2:
            print('YES')
            print(str(i + 1) + " " + str(int(i + len(necklace) / 2 + 1)))
            return True

    print('NO')
    return False


checker()