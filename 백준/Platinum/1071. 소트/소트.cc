#include <stdio.h>
int main() {
    int arr[50];
    int seq[50];
    int n;
    int tmp = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int ck = 0;
    for (int i = 0; i <= 1000; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[j] == i) {
                seq[ck] = i;
                ck++;
            }
        }
    }
    for (int i = 1; i < n; i++) {
        if (seq[i] - 1 == seq[i - 1]) {
            for (int j = 1; j < (n - i); j++) {
                if (seq[i + j] - 1 >= seq[i + j - 1]) {
                    tmp = seq[i + j];
                    seq[i + j] = seq[i + j - 1];
                    seq[i + j - 1] = tmp;
                    i = 0;
                    break;
                }
            }
        }
    }
    for (int i = 1; i < n; i++) {
        if (seq[i] - 1 == seq[i - 1]) {
            tmp = seq[i];
            seq[i] = seq[i - 1];
            seq[i - 1] = tmp;
            i = 0;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", seq[i]);
    }
    return 0;
}