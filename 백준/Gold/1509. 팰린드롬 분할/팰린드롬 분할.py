def palindrome(s):
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True
    for i in range(n - 1):
        is_palindrome[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            is_palindrome[start][end] = (s[start] == s[end]) and is_palindrome[start + 1][end - 1]

    dp = [float('inf')] * n
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 1
        else:
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]

s = input().strip()
print(palindrome(s))