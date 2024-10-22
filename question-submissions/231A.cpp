#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int tc;
    int a,b,c;
    int counter=0;
    cin >> tc;
    for(int i=0;i<tc;i++) {
        scanf("%d %d %d",&a,&b,&c);
        if (a+b+c>=2) {
            counter++;
        }
    }
    printf("%d",counter);
    return 0;
}