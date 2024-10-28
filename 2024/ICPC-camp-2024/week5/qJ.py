n,k = list(map(int, input().split()))
bag = list(map(int, input().split()))
values = []
for key in set(bag):
    values.append(bag.count(key))

values = sorted(values)[::-1]
counter=0

while sum(values)>0:
    val=0
    for i in range(len(values)):
        if val+values[-1]>k:
            break
        if val + values[i] <= k :
            val+=values[i]
            values[i]=0

    counter+=1
print(counter)