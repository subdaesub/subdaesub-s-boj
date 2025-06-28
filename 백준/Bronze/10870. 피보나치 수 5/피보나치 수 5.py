fib = [0, 1]
for i in range(2, 21):
    fib.append(fib[i - 2] + fib[i - 1])
n = int(input())
print(fib[n])