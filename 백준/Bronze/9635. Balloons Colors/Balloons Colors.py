import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    easy = arr[1]
    hard = arr[-1]

    problems = list(map(int, input().split()))

    if problems[0] == easy and problems[-1] == hard:
        print("BOTH")
    elif problems[0] == easy:
        print("EASY")
    elif problems[-1] == hard:
        print("HARD")
    else:
        print("OKAY")