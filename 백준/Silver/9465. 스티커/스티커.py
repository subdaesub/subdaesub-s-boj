import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    prevprev0, prevprev1 = 0, 0
    prev0, prev1 = sticker[0][0], sticker[1][0]

    for i in range(1, n):
        current0 = max(prev1, prevprev1) + sticker[0][i]
        current1 = max(prev0, prevprev0) + sticker[1][i]

        prevprev0, prevprev1 = prev0, prev1
        prev0, prev1 = current0, current1

    print(max(prev0, prev1))