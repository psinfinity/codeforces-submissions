#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    string guest,host,pile;
    cin >> guest >> host >> pile;
    string before_pile = guest+host;
    sort(before_pile.begin(),before_pile.end());
    sort(pile.begin(),pile.end());
    if (pile==before_pile) {
        printf("YES");
    } else printf("NO");
    return 0;
}