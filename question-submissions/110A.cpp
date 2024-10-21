#include <cstdio>
#include <string>
#include <iostream>
#include <string.h>
using namespace std;

int main() {
    char str[18];
    int counter;
    scanf("%s",str);
    for (int i=0;i<18;i++) {
        if (str[i]=='4' || str[i]=='7') {
            counter++;
        }
    }
    if (counter==4 || counter==7) {
        printf("YES");
        return 0;
    }
    printf("NO");
    return 0;
}