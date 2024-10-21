#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int contest_count;
    scanf("%d",&contest_count);
    int contest;
    scanf("%d",&contest);
    int min_contest = contest;
    int max_contest = contest;
    int amazing = 0;
    for (int i=0;i<contest_count-1;i++) {
        scanf("%d",&contest);
        if (contest < min_contest) {
            min_contest = contest;
            amazing++;
        } else if (contest > max_contest) {
            max_contest = contest;
            amazing++;
        }
    }
    printf("%d",amazing);
    return 0;
}