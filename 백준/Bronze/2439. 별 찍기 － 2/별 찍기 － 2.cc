#include <stdio.h>
int main() {
    int n, k, l;
    scanf("%d", &n);
    for (int i = 1; i < (n + 1); i++) {
        k = i;
        l = n - i;
        while (l > 0) {
            printf(" ");
            l--;
        }
        while (k > 0) {
            printf("*");
            k--;
        }
        printf("\n");
    }
    return 0;
}