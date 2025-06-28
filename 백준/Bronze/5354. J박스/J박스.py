import sys
input = sys.stdin.readline
clk = False
n = int(input())
for _ in range(n):
    k = int(input())
    if k == 1:
        print('#')
    else:
        print('#' * k)
        for i in range(k - 2):
            print('#' + ('J' * (k - 2) + '#'))
        print('#' * k)
    print('')