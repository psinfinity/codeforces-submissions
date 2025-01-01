for i in range(int(input())):
    n = int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))

    max_sum = 0
    max_second = -100000
    for j in range(n):
        max_sum+=max(list1[j],list2[j])
        max_second=max(min(list1[j],list2[j]),max_second)

    print(max_sum+max_second)