def self_num(n):
    cnt = n
    while n != 0:
        cnt += n % 10
        n //= 10

    return cnt

num = [False for _ in range(10001)]
for i in range(1, 9973):
    t = i
    while True:
        k = self_num(t)
        if k < 10001:
            t = k
            if not num[k]:
                num[k] = True
        else:
            break
for i in range(1, 10001):
    if not num[i]:
        print(i)