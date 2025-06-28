from collections import deque
import sys
input = sys.stdin.readline

def calc(n, a, op):
    q = deque()
    i = 0
    a.append(0)
    q.append((a[i], a[i + 1], op, i))
    result = []
    while q:
        ans, num, op, k = q.popleft()
        if sum(op) == 0:
            result.append(ans)
        else:
            if op[0] > 0:
                l = [op[0], op[1], op[2], op[3]]
                l[0] -= 1
                q.append((ans + num, a[k + 2], l, k + 1))

            if op[1] > 0:
                l = [op[0], op[1], op[2], op[3]]
                l[1] -= 1
                q.append((ans - num, a[k + 2], l, k + 1))

            if op[2] > 0:
                l = [op[0], op[1], op[2], op[3]]
                l[2] -= 1
                q.append((ans * num, a[k + 2], l, k + 1))

            if op[3] > 0:
                l = [op[0], op[1], op[2], op[3]]
                l[3] -= 1
                if ans >= 0:
                    q.append((ans // num, a[k + 2], l, k + 1))
                else:
                    q.append((-(-ans // num), a[k + 2], l, k + 1))

    return max(result), min(result)

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
max_ans, min_ans = calc(n, a, op)
print(max_ans)
print(min_ans)