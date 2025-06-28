n=int(input())
a = 0
k = 0
arr = [0] * 10
while True:
    if n==10 :
        arr[a] = 9
        arr[a+1] = 1
        a += 2
        break
    digit = len(str(n))
    x = int(digit / 2)
    if digit % 2 == 0:
        tmp = int(n / (10 ** x))
        k = int((str(tmp)[::-1]))
        k += (tmp * (10 ** x))
        if n - k < 0:
            tmp -= 1
            k = int((str(tmp)[::-1]))
            k += (tmp * (10 ** x))
        n = int(n - k)
    else:
        tmp = int(n / (10 ** x))
        k = int((str(tmp)[::-1]))
        k += (int(tmp / 10)) * (10 ** (x + 1))
        if n - k < 0:
            tmp -= 1
            k = int((str(tmp)[::-1]))
            if (len(str(n-1))!=digit) :
                k += (tmp * (10 ** x))
            else :
                k += (int(tmp / 10)) * (10 ** (x + 1))
        n = int(n - k)
    if k == 0:
        break
    arr[a] = k
    a += 1

print(a)
for i in range(10):
    if arr[i] != 0:
        print(arr[i])