#include <cmath>
#include <cstdio>
using namespace std;

int main() {
    int x {0};
    int y {0};
    for(int i=0;i<=24;i++) {
        int element;
        scanf("%d", &element);
        x = i%5;
        y = (i-i%5)/5;
        if (element==1) {
            printf("%d",abs(2-x)+abs(2-y));
            return 0;
        }
    }
    return 0;
}