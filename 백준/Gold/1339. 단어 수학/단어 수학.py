import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
weight = {}

for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        value = 10 ** (length - i - 1)
        weight[ch] = weight.get(ch, 0) + value

sorted_letters = sorted(weight.items(), key=lambda x: -x[1])

num = 9
digit = {}
for letter, _ in sorted_letters:
    digit[letter] = num
    num -= 1

total = 0
for word in words:
    num_str = ''.join(str(digit[ch]) for ch in word)
    total += int(num_str)

print(total)