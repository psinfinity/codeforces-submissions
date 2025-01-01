n = int(input())
mapper = []
place_holder = {}
for _ in range(n):
    mapper.append(input())

for row in range(n):
    for column in range(n):
        if mapper[row][column] == '#':
            if (row,column) in place_holder:
                del place_holder[row,column]
            else:
                if (row+1,column-1) not in place_holder and (row+1,column) not in place_holder and (row+1,column+1) not in place_holder and (row+2,column) not in place_holder:
                    place_holder[row+1,column-1]=True
                    place_holder[row+1, column] = True
                    place_holder[row+1, column+1] = True
                    place_holder[row+2, column] = True

if len([True for key in place_holder.keys() if place_holder[key]==True])==0:
    print("YES")
else:
    print("NO")