#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;

int main() {
    char bin1[300];
    char bin2[300];
    cin >> bin1;
    cin >> bin2;

    for (int i=0;i<strlen(bin1);i++) {
        if (bin1[i]==bin2[i]) {
            cout << "0";
        } else {
            cout << "1";
        }
    }

    return 0;
}