n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(0)
else:
    a = n // 2
    b = n % 2
    if b == 1:
        print('4' + '8' * a)
    else:
        print('8' * a)