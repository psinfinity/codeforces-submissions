#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int stop;
    scanf("%d",&stop);
    int a,b;
    int sum = 0;
    int max_sum = 0;
    for (int i=0;i<stop;i++) {
        scanf("%d %d",&a,&b);
        sum+=b-a;
        if (sum>max_sum) {
            max_sum=sum;
        }
    }
    printf("%d",max_sum);
    return 0;
}