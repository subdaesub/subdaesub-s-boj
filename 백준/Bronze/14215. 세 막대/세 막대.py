k = list(map(int, input().split()))
if max(k) >= (sum(k) - max(k)):
    print(2 * sum(k) - 2 * max(k) - 1)
else:
    print(sum(k))