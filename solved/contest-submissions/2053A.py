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
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        if arr[i]<2*arr[i+1] and arr[i+1]<2*arr[i]:
            print("YES")
            return True
    print("NO")
    return False

for _ in range(int(input())):
    solve()