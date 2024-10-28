#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;

    for(int i=0;i<200;i++) {
        if (str[i]=='.' or str[i]=='-') {
            if (str[i]=='.') {
                printf("0");
            } else {
                i++;
                if (str[i]=='.') {
                    printf("1");
                } else {
                    printf("2");
                }
            }
        } else {
            return 0;
        }
    }

}