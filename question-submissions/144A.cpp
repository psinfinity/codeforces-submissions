#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int n;
    int soldier;
    scanf("%d",&n);
    scanf("%d",&soldier);

    int min = soldier;
    int max = soldier;
    int min_loc = 1;
    int max_loc = 1;

    for (int i=2;i<=n;i++) {
        scanf("%d",&soldier);
        if (soldier>max) {
            max = soldier;
            max_loc = i ;
        }
        if (soldier<=min) {
            min = soldier;
            min_loc = i;
        }
    }
    int k=0;
    if (min_loc < max_loc) {
        k=1;
    }
    printf("%d",max_loc-1+n-min_loc-k);
    return 0;
}