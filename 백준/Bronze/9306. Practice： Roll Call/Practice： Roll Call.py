import sys
input = sys.stdin.readline

x = int(input())

for i in range(1, x + 1):
    a = input().strip()
    b = input().strip()

    print(f"Case {i}: {b}, {a}")