# -*- coding: utf-8 -*-
"""
0枚以上使ってN円を支払う
使う効果の枚数として考えられる最小値

合計9999円枚以下の効果で支払えるという親切な文言がヒント
Cの枚数は自然と決まりそうだけど問題はPythonで10**8が間に合うかという心配
"""
N = int(input())
A, B, C = list(map(int, input().split()))

ans = 100001
for a in range(10000):
    for b in range(10000-a):
        cur = a * A + b * B
        rest = N-cur
        if rest < 0:
            break
        if rest == 0:
            ans = min(ans, a+b)
            break
        if rest % C == 0:
            c = rest // C
            ans = min(ans, a+b+c)
print(ans)
