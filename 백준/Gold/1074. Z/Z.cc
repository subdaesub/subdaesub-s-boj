#include <stdio.h>
int main() {
    int n, r, c;
    scanf("%d %d %d", &n, &r, &c);
    int t = 1;
    for (int i = 0; i < n; i++) {
        t *= 2;
    }
    int max = t * t;
    for (int i = 0; i < n; i++) {
        if (r < (t / 2) && c < (t / 2)) {
            r = r;
            c = c;
            max -= (t * t / 4 * 3);
        }
        else if (r < (t / 2) && c >= (t / 2)) {
            r = r;
            c -= (t / 2);
            max -= (t * t / 4 * 2);
        }
        else if (r >= (t / 2) && c < (t / 2)) {
            r -= (t / 2);
            c = c;
            max -= (t * t / 4 * 1);
        }
        else {
            r -= (t / 2);
            c -= (t / 2);
            max = max;
        }
        t /= 2;
    }
    printf("%d", max - 1);
    return 0;
}