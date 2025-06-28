n = input()
f = int(input())
n = n[:-2]
for i in range(100):
    if i < 10:
        k = int(n + '0' + str(i))
        if k % f == 0:
            print('0' + str(i))
            break
    else:
        k = int(n + str(i))
        if k % f == 0:
            print(str(i))
            break