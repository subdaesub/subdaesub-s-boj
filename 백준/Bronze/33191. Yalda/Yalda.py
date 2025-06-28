a=[]
for _ in range(4):
    a.append(int(input()))
if a[1] <= a[0]:
    print('Watermelon')
elif a[2] <= a[0]:
    print('Pomegranates')
elif a[3] <= a[0]:
    print('Nuts')
else:
    print('Nothing')