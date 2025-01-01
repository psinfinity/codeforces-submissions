#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int drinks;
    scanf("%d",&drinks);
    double sum = 0;
    float element;
    for (int i=0;i<drinks;i++) {
        scanf("%f",&element);
        sum+=element;
    }
    double mean = sum/drinks;
    cout << mean;

    return 0;
}