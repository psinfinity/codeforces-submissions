# https://codeforces.com/problemset/problem/174/A
import sys

nb = [int(x) for x in sys.stdin.readline().split()]
# n = total number of friends
# b = current volume of drink in the bottle

def min_amount_needed(my_list):
    return sum([max(my_list)-x for x in my_list])

friend_drinks = [int(x) for x in sys.stdin.readline().split()]

if nb[1]>=min_amount_needed(friend_drinks):
    for j in [(nb[1]-min_amount_needed(friend_drinks))/nb[0] + max(friend_drinks)-i for i in friend_drinks]:
        print(format(j,'.6f'))
else:
    print(-1)