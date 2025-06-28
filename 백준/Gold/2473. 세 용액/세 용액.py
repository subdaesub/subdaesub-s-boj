import sys
input = sys.stdin.readline

def three(arr):
    arr.sort()
    n = len(arr)
    gozero = float('inf')
    result = []

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if abs(total) < abs(gozero):
                gozero = total
                result = [arr[i], arr[left], arr[right]]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return sorted([arr[i], arr[left], arr[right]])

    return sorted(result)

n = int(input())
liquid = list(map(int, input().split()))

print(*three(liquid))