'''
                                             +*****+
                                         ***+       +*+
                                      ***              +*+    +**=  +*+            =+++++=
                                   +**+                   +**+         **     =+++         =++=
                      *#*        ***           ***           +*++        **+                   +=
                     ####      **+            +###                           =*+                =+
                     #############################                               *+              ==
                      ****************************                                 +*+            +
                   =++############***############# ##+++++++++++++=                     ++       +
                +*++ #########*##****###*#########+###*#* **             =+++++++=          =+= =
              +*+    ########*#*        *#*#######+###*#**** ** +*= ++                  =======
             +*       *******##          #********+###*#**** **-+*+++++++++====- ==  -::--::--::
             +*       *#######*          ########=+##**#**** **=+*==++==+--+: ======-
             +*=      *########       =+=########=+##+*#++** ** ++= ++====-
               +*+++  *#######*+**+++====######## +###*#**** **====
                      *#######*=++===    ######## +###*#**++==
                      *########          ######## +##*+++=
                     =+########          ######## +++==
                    =++********          ********====
                    =+==                       ==+=
                      -==+===                 ==+=
                            ===+++=====       ===
                                    -====+=+++'''
import sys
input = sys.stdin.readline #input

def min_max_subarray_sum(arr:list)-> tuple: # Kadane's Algorithm
    best_max = 0
    max_sum = 0
    best_min = 0
    min_sum = 0
    for ele in arr:
        max_sum = max(ele,max_sum+ele)
        best_max = max(best_max,max_sum)
        min_sum = min(ele,min_sum+ele)
        best_min = min(best_min,min_sum)
    return best_min, best_max

def post_subarray_sum_anchored(arr:list,i)-> tuple:
    best_max = 0
    best_min = 0
    curr_sum = 0
    for ele in arr[i+1:]:
        curr_sum+=ele
        best_max = max(curr_sum,best_max)
        best_min = min(curr_sum,best_min)
    return best_min, best_max

def pre_subarray_sum_anchored(arr:list,i)-> tuple:
    curr_sum = sum(arr[:i])
    best_max = curr_sum
    best_min = curr_sum
    curr_sum = sum(arr[:i])
    for ele in arr[:i]:
        curr_sum-=ele
        best_max = max(curr_sum,best_max)
        best_min = min(curr_sum,best_min)
    return best_min, best_max

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    x = None

    for i in range(n): # finding x
        if abs(arr[i]) != 1:
            x = i
            break

    if x is None:
        val = min_max_subarray_sum(arr)
        print(val[1]-val[0]+1)
        return list(range(val[0], val[1]+1))

    part1 = min_max_subarray_sum(arr[:x])
    part2 = min_max_subarray_sum(arr[x+1:])
    part1x = pre_subarray_sum_anchored(arr,x)
    part2x = post_subarray_sum_anchored(arr,x)
    total = []
    total.extend(list(range(part1[0],part1[1]+1)))
    total.extend(list(range(part2[0],part2[1]+1)))
    total.extend(list(range(part1x[0]+arr[x]+part2x[0],part1x[1]+arr[x]+part2x[1]+1)))
    total = sorted(list(set(total)))
    print(len(total))
    return total

for _ in range(int(input())):
    for i in solve():
        print(i,end=" ")
    print()