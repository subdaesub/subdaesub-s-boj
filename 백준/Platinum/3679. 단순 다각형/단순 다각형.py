import math
import sys
input = sys.stdin.readline

def sort_points(points):

    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)
    
    sorted_points = sorted(enumerate(points), key=lambda p: math.atan2(p[1][1] - cy, p[1][0] - cx))
    
    return [p[0] for p in sorted_points]

c = int(input())
results = []

line = 1
for _ in range(c):
    test_case = list(map(int, input().split()))
    line += 1
    
    n = test_case[0]
    points = [(test_case[i * 2 + 1], test_case[i * 2 + 2]) for i in range(n)]
    
    result = sort_points(points)
    results.append(" ".join(map(str, result)))

for i in results:
    print(i)