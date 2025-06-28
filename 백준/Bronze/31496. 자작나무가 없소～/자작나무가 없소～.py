import sys
input = sys.stdin.readline

n, item = map(str, input().split())
cnt = 0
for _ in range(int(n)):
    *items, last = input().split('_')
    last_item, num = last.split()
    items.append(last_item)
    if item in items:
        cnt += int(num)

print(cnt)