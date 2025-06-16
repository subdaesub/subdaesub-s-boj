import sys
input = sys.stdin.readline

thirtysix = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def convert(arr, k):
    gap = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][-j - 1] == k:
                gap += (thirtysix.index('Z') - thirtysix.index(k)) * (36 ** j)
    return gap


n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())
k = int(input())
sum = 0
ans = ''

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][-j - 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            sum += int(arr[i][-j - 1]) * (36 ** j)
        else:
            sum += (ord(arr[i][-j - 1]) - ord('A') + 10) * (36 ** j)

changed = []

for i in thirtysix:
    changed.append(convert(arr, i))


for i in range(k):
    max_index = changed.index(max(changed))
    if changed[max_index] == 0:
        break

    sum += changed[max_index]
    changed[max_index] = 0

while sum != 0:
    ans = thirtysix[sum % 36] + ans
    sum //= 36

if ans == '':
    ans = '0'
print(ans)