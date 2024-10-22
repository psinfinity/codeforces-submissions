#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    string element;
    cin >> element;
    for (char i:element) {
        if (i=='H'||i=='Q'||i=='9') {
            printf("YES");
            return 0;
        }
    }
    printf("NO");
    return 0;
}