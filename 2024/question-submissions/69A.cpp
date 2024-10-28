#include <cstdio>
using namespace std;

int main() {
    int sum_i=0;
    int sum_j=0;
    int sum_k=0;
    int tc;
    scanf("%d", &tc);
    for(int i = 0; i<tc; i++) {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        sum_i+=a;
        sum_j+=b;
        sum_k+=c;
    }
    if (sum_i==0 && sum_j==0 && sum_k==0) {
        printf("YES");
    } else {
        printf("NO");
    }
    return 0;
}
