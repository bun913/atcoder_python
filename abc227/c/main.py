"""
A <= B <= Cかつ A * B* C <=N であるような正の整数の組みの数を求める
Nが10**11以下であることは保証されている
ということは、制約からAは10**4以下であることは保証されている
"""
N = int(input())
ans = 0
a = 1
while a ** 3 <= N:
    b = a
    b_limit = int((N / a) ** (1/2)) + 1
    while a * b ** 2 <= N:
        c = N // (a*b)
        if c < b:
            break
        cnt = c - b + 1
        ans += cnt
        b += 1
    a += 1

print(ans)
