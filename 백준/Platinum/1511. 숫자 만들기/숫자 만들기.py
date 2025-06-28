num = list(map(int, input().split()))

def zeromax(ans, num):
    ans += '0'
    for i in range(9, 0, -1):
        if num[i] > 0:
            while num[i] != 0:
                ans += str(i)
                num[i] -= 1
                ans += '0'
    return ans
def findmax(num):
    for i in range(9, -1, -1):
        if num[i] > 0:
            return i

ans = ''

i = findmax(num)

while True:
    if sum(num) == 0:
        break
    elif num[0] > sum(num[1:]):
       ans = zeromax(ans, num)
       break
    else:
        if max(num) != num[i] and max(num) > sum(num) - max(num):
            i = num.index(max(num))
            ans += str(i)
            num[i] -= 1
        else:
            if num[i] > 0:
                ans += str(i)
                num[i] -= 1
            else:
                i = findmax(num)
                if ans[-1] != str(i):
                    ans += str(i)
                    num[i] -= 1

        if num[0] > sum(num[1:]):
            ans = zeromax(ans, num)
            break
        if max(num) != num[i] and max(num) > sum(num) - max(num):
            i = num.index(max(num))
            ans += str(i)
            num[i] -= 1

        for k in range(9, -1, -1):
            if k == i:
                pass
            else:
                if num[k] > 0:
                    ans += str(k)
                    num[k] -= 1
                    break
        if len(ans) > 1:
            if ans[-1] == ans[-2]:
                ans = ans[:-1]
                break
if int(ans) == 0:
    print(0)
elif ans[0] == '0':
    print(ans[1:])
else:
    print(ans)