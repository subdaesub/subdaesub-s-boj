n=int(input())
s=input()
for i in s:
    if i == 'J':
        print('O', end='')
    elif i == 'O':
        print('I', end='')
    else:
        print('J', end='')