dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dig(x):
    while x >= 10:
        x = sum(int(digit) for digit in str(x))
    return x

def find(k, m):
    x, y = 0, 0
    w = 0
    dig_val = 1
    
    visited = {}
    steps = []

    for cnt in range(1, k + 1):
        if (x, y, w) in visited:
            steps.append((x, y))
            cycle_start = visited[(x, y, w)]
            cycle_length = cnt - cycle_start
            remaining_steps = (k - cycle_start) % cycle_length
            return steps[cycle_start + remaining_steps]
        
        visited[(x, y, w)] = cnt
        steps.append((x, y))

        x += dx[w] * dig_val
        y += dy[w] * dig_val

        w = (w + 1) % 4

        dig_val = dig(dig_val * m)

    return (x, y)

t = int(input())
for _ in range(t):
    k, m = map(int, input().split())
    print(find(k, m)[0], find(k, m)[1])