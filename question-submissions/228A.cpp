#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    long int a,b,c,d;
    scanf("%d %d %d %d",&a,&b,&c,&d);
    if (a==b && c==d && b==c) {
        cout << 3;
    } else if (a==b && b==c || b==c && c==d || a==d && d==c || a==b && b==d) {
        cout << 2;
    } else if ((a==b && c==d) || (a==c && b==d) || (a==d && b==c)) {
        cout << 2;
    } else if (a==b || a==c || a==d || c==b || d==b || c==d) {
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}