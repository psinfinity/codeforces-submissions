#include <cstdio>
using namespace std;

int main() {
    int toggle_arr[3][3] {
        {0,0,0},
        {0,0,0},
        {0,0,0}
    };

    for (int i = 0 ; i<9; i++) {
        int element;
        scanf("%d",&element);
        if (element%2==1) {
            switch(i) {
                case 0:
                    toggle_arr[0][0]++;
                    toggle_arr[0][1]++;
                    toggle_arr[1][0]++;
                    break;
                case 1:
                    toggle_arr[0][0]++;
                    toggle_arr[0][1]++;
                    toggle_arr[0][2]++;
                    toggle_arr[1][1]++;
                    break;
                case 2:
                    toggle_arr[0][2]++;
                    toggle_arr[0][1]++;
                    toggle_arr[1][2]++;
                    break;
                case 3:
                    toggle_arr[0][0]++;
                    toggle_arr[1][1]++;
                    toggle_arr[1][0]++;
                    toggle_arr[2][0]++;
                    break;
                case 4:
                    toggle_arr[1][1]++;
                    toggle_arr[0][1]++;
                    toggle_arr[1][0]++;
                    toggle_arr[2][1]++;
                    toggle_arr[1][2]++;
                    break;
                case 5:
                    toggle_arr[0][2]++;
                    toggle_arr[1][1]++;
                    toggle_arr[1][2]++;
                    toggle_arr[2][2]++;
                    break;
                case 6:
                    toggle_arr[1][0]++;
                    toggle_arr[2][1]++;
                    toggle_arr[2][0]++;
                    break;
                case 7:
                    toggle_arr[2][0]++;
                    toggle_arr[2][1]++;
                    toggle_arr[2][2]++;
                    toggle_arr[1][1]++;
                    break;
                case 8:
                    toggle_arr[2][1]++;
                    toggle_arr[2][2]++;
                    toggle_arr[1][2]++;
                    break;
                default:
                    break;
            }
        }

    }
    for (int i=0;i<3;i++) {
        for (int j=0;j<3;j++) {
            toggle_arr[i][j]++;
            printf("%d",toggle_arr[i][j]%2);
        }
        printf("\n");
    }

    return 0;
}