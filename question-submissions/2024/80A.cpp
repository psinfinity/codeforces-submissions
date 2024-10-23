#include <cstdio>
using namespace std;

int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    for (n++;n<=m;n++) {
        for (int i=2;i<n;i++) {
            if (n%i==0) {
                break;
            }
            if (n<m && i==n-1) {
                printf("NO");
                return 0;
            }
            if (n==m && i==n-1) {
                printf("YES");
                return 0;

            }
        }
    }
    printf("NO");
    return 0;
}