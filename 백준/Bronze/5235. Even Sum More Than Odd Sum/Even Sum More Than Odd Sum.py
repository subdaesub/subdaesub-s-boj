t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    cnt_even = 0
    cnt_odd = 0
    for i in arr:
        if i % 2 == 0:
            cnt_even += i
        else:
            cnt_odd += i
    if cnt_even > cnt_odd:
        print('EVEN')
    elif cnt_odd > cnt_even:
        print('ODD')
    else:
        print('TIE')