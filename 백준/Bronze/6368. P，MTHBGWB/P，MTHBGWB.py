import sys
input = sys.stdin.readline

code = {'A':'.-', 'B': '-...', 'C': '-.-.', 'D':'-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '_': '..--', '.': '---.', ',': '.-.-', '?' : '----'}

t = int(input())
for j in range(1, t + 1):
    s = input().strip()
    morse = ''
    length = ''
    for i in range(len(s)):
        morse += code[s[i]]
        length += str(len(code[s[i]]))
    
    length = length[::-1]

    cnt = 0

    print(f'{j}: ', end ='')
    for i in range(len(length)):
        for key, value in code.items():
            if value == morse[cnt:cnt + int(length[i])]:
                print(key, end = '')
        cnt += int(length[i])
    print('')