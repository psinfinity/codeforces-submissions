#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int cupboards;
    int r_sum = 0;
    int l_sum = 0;
    int r_cup,l_cup;
    scanf("%d", &cupboards);
    for (int i = 0; i<cupboards; i++) {
        scanf("%d %d",&r_cup,&l_cup);
        r_sum+=r_cup;
        l_sum+=l_cup;
    }

    printf("%d",min(r_sum,cupboards-r_sum) + min(l_sum,cupboards-l_sum));
    return 0;
}