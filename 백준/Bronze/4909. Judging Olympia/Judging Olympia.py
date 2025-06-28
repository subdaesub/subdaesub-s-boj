while True:
    l = list(map(int, input().split()))
    if sum(l) == 0:
        break    
    l.sort()
    l = l[1:5]
    if sum(l) % 4 == 0:
        print(sum(l) // 4)
    else:
        print(sum(l) / 4)