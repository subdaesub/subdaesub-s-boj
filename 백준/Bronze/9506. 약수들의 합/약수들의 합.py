def perfect(k):
    arr = []
    for i in range(1, k // 2 + 1):
        if k % i == 0:
            arr.append(i)

    return arr

while True:
    n = int(input())
    if n == -1:
        break
    if sum(perfect(n)) == n:
        print(f'{n} = ', end = '')
        print(" + ".join(map(str, perfect(n))))
    else:
        print(f'{n} is NOT perfect.')