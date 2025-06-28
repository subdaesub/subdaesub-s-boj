fib = [0, 1]
for i in range(39):
  fib.append(fib[i] + fib[i + 1])
n = int(input())
print(fib[n], n-2)