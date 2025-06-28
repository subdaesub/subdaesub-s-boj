fib = [0, 1]
for i in range(89):
  fib.append(fib[i] + fib[i + 1])
n = int(input())
print(fib[n])