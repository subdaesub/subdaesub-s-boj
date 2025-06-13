import sys
input = sys.stdin.readline

s = input()

key1 = 'CHIPMUNKS'
key2 = 'LIVE'

code = 0

arr1 = ['' for _ in range(26)]
arr2 = ['' for _ in range(26)]

for i in range(26):
    for ch in key1:
        if ord(ch) + i < 65 + 26:
            arr1[i] += chr(ord(ch) + i)
        else:
            arr1[i] += chr(ord(ch) + i - 26)

    for ch in key2:
        if ord(ch) + i < 65 + 26:
            arr2[i] += chr(ord(ch) + i)
        else:
            arr2[i] += chr(ord(ch) + i - 26)

for i in range(26):
    for j in range(len(s) - 3):
        if s[j:j + 4] == arr2[i]:
            for k in range(len(s) - 8):
                if s[k:k + 9] == arr1[i]:
                    code = i
                    break

for ch in s:
    if ord(ch) >= 65 and ord(ch) <= 90:  # A-Z
        if ord(ch) - code >= 65:
            print(chr(ord(ch) - code), end='')
        else:
            print(chr(ord(ch) - code + 26), end='')
    else:
        print(ch, end='')