import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    numerator, denominator = map(int, input().split())

    integer_part = numerator // denominator
    remainder = numerator % denominator

    digits = []
    remainder_pos = {}

    repeating_start = None
    index = 0

    remainder *= 10

    while True:
        if remainder == 0:
            break

        if remainder in remainder_pos:
            repeating_start = remainder_pos[remainder]
            break

        remainder_pos[remainder] = index
        digit = remainder // denominator
        digits.append(digit)
        remainder = (remainder % denominator) * 10
        index += 1

    if remainder == 0:
        if digits:
            decimal_part = ''.join(map(str, digits)) + '(0)'
        else:
            decimal_part = '(0)'
    else:
        non_repeating_digits = digits[:repeating_start]
        repeating_digits = digits[repeating_start:]

        decimal_part = f"{''.join(map(str, non_repeating_digits))}({''.join(map(str, repeating_digits))})"

    print(f"{integer_part}.{decimal_part}")