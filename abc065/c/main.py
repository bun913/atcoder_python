"""

"""


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i % MOD
    return result


N, M = map(int, input().split())
MOD = 10 ** 9 + 7

# 多い方をaとする
a, b = max(N, M), min(N, M)

if abs(a-b) >= 2:
    print(0)
    exit()

if abs(a-b) == 1:
    print(fact(a) * fact(b) % MOD)
    exit()

print(fact(a) * fact(b) * 2 % MOD)
