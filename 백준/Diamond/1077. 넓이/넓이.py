def cross(o, a, b):

    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_point_inside(p, polygon):

    n = len(polygon)
    inside = False
    x, y = p
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def line_intersection(p1, p2, q1, q2):

    A1, B1, C1 = p2[1] - p1[1], p1[0] - p2[0], cross((0, 0), p2, p1)
    A2, B2, C2 = q2[1] - q1[1], q1[0] - q2[0], cross((0, 0), q2, q1)
    det = A1 * B2 - A2 * B1
    if det == 0:
        return None
    x = (B2 * -C1 - B1 * -C2) / det
    y = (A1 * -C2 - A2 * -C1) / det
    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(q1[0], q2[0]) <= x <= max(q1[0], q2[0]):
        if min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]) and min(q1[1], q2[1]) <= y <= max(q1[1], q2[1]):
            return (x, y)
    return None

def polygon_intersection(poly1, poly2):

    intersection_points = []
    n, m = len(poly1), len(poly2)

    for i in range(n):
        for j in range(m):
            p1, p2 = poly1[i], poly1[(i + 1) % n]
            q1, q2 = poly2[j], poly2[(j + 1) % m]
            inter = line_intersection(p1, p2, q1, q2)
            if inter:
                intersection_points.append(inter)

    for point in poly2:
        if is_point_inside(point, poly1):
            intersection_points.append(point)

    for point in poly1:
        if is_point_inside(point, poly2):
            intersection_points.append(point)
    
    intersection_points = list(set(intersection_points))
    if not intersection_points:
        return []
    
    cx = sum(p[0] for p in intersection_points) / len(intersection_points)
    cy = sum(p[1] for p in intersection_points) / len(intersection_points)
    intersection_points.sort(key=lambda p: (math.atan2(p[1] - cy, p[0] - cx)))
    
    return intersection_points

def polygon_area(polygon):

    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

poly1 = [tuple(map(int, input().split())) for i in range(n)]
poly2 = [tuple(map(int, input().split())) for i in range(m)]

intersection = polygon_intersection(poly1, poly2)

if not intersection:
    print(0.0)
else:
    print(f"{polygon_area(intersection):.9f}")