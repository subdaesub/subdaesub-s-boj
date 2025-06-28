n = int(input())
quote = []
for _ in range(n):
    quote.append(input())
k = int(input())
for i in range(k):
    s = int(input())
    if s >= 1 and s <= n:
        print(f"Rule {s}: {quote[s - 1]}")
    else:
        print(f"Rule {s}: No such rule")