#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n, k, l, c, d, p, nl, np;
    scanf("%d %d %d %d %d %d %d %d",&n,&k,&l,&c,&d,&p,&nl,&np);
    int toasts = min(floor((k*l)/(n*nl)), floor(d*c/n));
    toasts = min(floor(toasts), floor(p/(n*np)));
    printf("%d",toasts);
    return 0;
}