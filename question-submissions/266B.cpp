#include <cstdio>
#include <string>
using namespace std;

int main() {
    int n,t;
    scanf("%d %d",&n,&t);
    char line[n];
    scanf("%s",line);
    while (t>0) {
        for(int i=0;i<n-1;i++) {
            if (line[i]=='B' && line[i+1]=='G') {
                line[i] = 'G';
                line[i+1] = 'B';
                i++;
            }
        }
    t--;
    }

    printf("%s",line);
    return 0;
}