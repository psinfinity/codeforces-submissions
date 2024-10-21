#include <cstdio>
using namespace std;

int main() {
    int year;
    scanf("%d",&year);
    year++;
    int d = year%10;
    int c = (year%100 - d)/10;
    int b = (year%1000 - c - d)/100;
    int a = (year - b - c - d) / 1000;
    while (a==b || b==c || c==d || a==d || b==d || a==c) {
        year++;
        d = year%10;
        c = (year%100 - d)/10;
        b = (year%1000 - c - d)/100;
        a = (year - b - c - d)/1000;
    }
    printf("%d",year);
    return 0;
}