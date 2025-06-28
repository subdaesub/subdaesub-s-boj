import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
current_sum = 0
min_len = float('inf')

while end < N:
    current_sum += arr[end]
    end += 1

    while current_sum >= S:
        min_len = min(min_len, end - start)
        current_sum -= arr[start]
        start += 1

print(min_len if min_len != float('inf') else 0)