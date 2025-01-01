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

def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def solve():
    n = int(input())
    values = []
    ans = ['0']*n
    taken_values = {}
    for i in range(n):
        l,r = map(int,input().split())
        if l==r:
            values.append(l)
            if l in taken_values:
                taken_values[l]+=1
            else:
                taken_values[l]=1
        else:
            values.append((l,r))

    taken_val = sorted(list(taken_values.keys()))
    for i in range(n):
        if type(values[i]) is int:
            if taken_values[values[i]]==1:
                ans[i] = '1'
            continue
        else:
            l_index = binary_search(taken_val,values[i][0])
            r_index = binary_search(taken_val,values[i][1])
            if l_index is False or r_index is False:
                ans[i] = '1'
                continue
            elif r_index-l_index != values[i][1]-values[i][0]:
                ans[i] = '1'
                continue

    return "".join(ans)

for _ in range(int(input())):
    print(solve())