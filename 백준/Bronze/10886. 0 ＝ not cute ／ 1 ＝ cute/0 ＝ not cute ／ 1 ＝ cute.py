n = int(input())
yes = 0
no = 0
for _ in range(n):
    k = int(input())
    if k == 1:
        yes += 1
    else:
        no += 1
    if yes > (n // 2):
        print('Junhee is cute!')
        break
    elif no > (n // 2):
        print('Junhee is not cute!')
        break