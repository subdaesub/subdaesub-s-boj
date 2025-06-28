a, b, c = map(int, input().split())
if b > c:
    b, c = c, b
    
x, y = map(int, input().split())
if x > y:
    x, y = y, x
    
if (b < x and x < c) and (b < y and y < c):
    print('City')
elif (x <= b and y <= b) or (c <= x and c <= y):
    print('Outside')
else:
    print('Full')