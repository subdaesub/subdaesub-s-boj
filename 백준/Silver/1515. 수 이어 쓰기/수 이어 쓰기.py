def solve(s):
    i = 1
    j = 0
    while True:
        for c in str(i):
            if j < len(s) and s[j] == c:
                j += 1
        if j == len(s):
            return i
        i += 1

s = input().strip()
print(solve(s))
