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
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = []

    a_val = {}
    for i in range(n):
        a_val[i] = a[i]
    sorted_a = sorted(list(a_val.keys()),key = lambda ele: a_val[ele]) # converts sorted to original
    b.sort()
    rev_a_val = {}
    for i in range(n):
        rev_a_val[sorted_a[i]] = i

    prod = 1
    for i in range(n):
        prod*=min(rev_a_val[i],b[i])
    ans.append(str(prod%998244353))


    for j in range(q):
        o,x = map(int,input().split())
        prod//=min(sorted_a[x-1],b[x-1])
        if o==1:
            a[x-1]+=1
        else:
            b[x-1]+=1
        b = organised(b,a)
        prod*=min(a[x-1],b[x-1])

        ans.append(str(prod%998244353))
    print(" ".join(ans))


for _ in range(int(input())):
    solve()