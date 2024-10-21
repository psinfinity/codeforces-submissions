#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int element;
    scanf("%d",&element);
    if (element%2==1) {
        printf("-1");
        return 0;
    }
    element/=2;
    for (int i=1;i<=element;i++) {
        printf("%d %d ",2*i,2*i-1);
    }
    return 0;
}