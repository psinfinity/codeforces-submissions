#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int arr_len;
    scanf("%d",&arr_len);
    char arr[arr_len];
    for (int j=0;j<arr_len;j++) {
        cin >> arr[j];
    }
    int counter = 0;
    for (int i=0;i<arr_len-1;i++) {
        if (arr[i]==arr[i+1]) {
            counter++;
        }
    }
    printf("%d",counter);
    return 0;
}