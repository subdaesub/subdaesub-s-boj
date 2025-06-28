def mat_mult(a, b, mod):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod,
         (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod,
         (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod]
    ]


def mat_pow(mat, exp, mod):
    result = [[1, 0], [0, 1]]
    while exp:
        if exp % 2:
            result = mat_mult(result, mat, mod)
        mat = mat_mult(mat, mat, mod)
        exp //= 2
    return result


def solve():
    m, a, c, x0, n, g = map(int, input().split())

    mat = [[a % m, c % m],
           [0, 1]]

    mat_n = mat_pow(mat, n, m)

    xn = (mat_n[0][0] * x0 + mat_n[0][1]) % m

    print(xn % g)

solve()