def hanoi(start, end, middle, plate, n):
    if n == 1:
        plate.append([start, end])
    else:
        hanoi(start, middle, end, plate, n - 1)
        plate.append([start, end])
        hanoi(middle, end, start, plate, n - 1)

n = int(input())
plate = []
hanoi(1, 3, 2, plate, n)

print(len(plate))
for i in plate:
    print(*i)