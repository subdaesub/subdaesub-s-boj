def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    print(a * b // GCD(a, b))

a, b = map(int, input().split())
LCM(a, b)