import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (len(arr) * 4)


def init(start, end, index):

    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2

    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]


def interval_sum(start, end, index, left, right):

    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, what, diff):
    if what < start or what > end:
        return
    tree[index] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, diff)
    update(mid + 1, end, index * 2 + 1, what, diff)


init(0, n - 1, 1)

for _ in range(m + k):
    command, b, c = map(int, input().split())
    if command == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(0, n - 1, 1, b, diff)
    else:
        print(interval_sum(0, n - 1, 1, b - 1, c - 1))