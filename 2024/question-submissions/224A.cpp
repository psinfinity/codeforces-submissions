#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    long double a,b,c;
    cin >> a >> b >> c;

    long double product_of {sqrt(a*b*c)};
    long double sum_of {(product_of/a) + (product_of/b) + (product_of/c)};

    cout << 4*sum_of;

    return 0;
}