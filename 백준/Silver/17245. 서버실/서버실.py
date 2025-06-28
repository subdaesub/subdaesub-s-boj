import sys
input = sys.stdin.readline

n = int(input())
num = 0
heights = []

for _ in range(n):
    row = list(map(int, input().split()))
    num += sum(row)
    heights.extend(row)

heights.sort()

target = (num + 1) // 2

left, right = 0, heights[-1]

while left < right:
    mid = (left + right) // 2
    active = sum(min(h, mid) for h in heights)

    if active >= target:
        right = mid
    else:
        left = mid + 1
        
print(left)