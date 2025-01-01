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

def solve():
    n,k = map(int,input().split())
    arr = sorted(list(map(int,input().split())))[::-1]
    arr_sum = 0
    for i in range(n):
        if arr_sum+arr[i]>k:
            break
        elif arr_sum+arr[i]==k:
            arr_sum += arr[i]
            break
        else:
            arr_sum+=arr[i]
    print(k-arr_sum)

for _ in range(int(input())):
    solve()