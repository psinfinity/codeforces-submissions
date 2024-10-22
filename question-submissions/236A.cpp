#include <iostream>
using namespace std;

int main() {
    string username;
    char element;
    getline(cin, username);
    int counter = 0;

    for (int i=1;i<username.length();i++) {
        for (int j=0;j<i;j++) {
            if (username[i]==username[j]) {
                counter++;
                break;
            }
        }
    }
    if ((username.length()-counter)%2==1) {
        cout << "IGNORE HIM!";
    } else {
        cout << "CHAT WITH HER!";
    }
    return 0;
}