#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int tc,n;
    scanf("%d",&tc);
    for (int i=0;i<tc;i++) {
        scanf("%d",&n);
        int min_arr[2*n-1] = {0};
        int element;

        for (int j=0;j<n;j++) {
            for (int k=0;k<n;k++) {
                scanf("%d",&element);
                if (element<min_arr[n-1+k-j]) {
                    min_arr[n-1+k-j]=element;
                }
            }
        }
        long int sum {0};
        for (int i:min_arr) {
            sum-=i;
        }
        printf("%d\n",sum);
    }
    return 0;
}