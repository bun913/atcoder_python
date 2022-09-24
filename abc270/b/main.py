# -*- coding: utf-8 -*-
"""
"""
# 不可能な場合を先に考える
X, Y, Z = list(map(int, input().split()))
if X > 0:
    if 0 < Y and Y < X:
        if Y < Z:
            print(-1)
            exit()
else:
    if Y < 0 and X < Y:
        if Z < Y:
            print(-1)
            exit()
ans = abs(X)
# 先にハンマーを別方向に拾いに行く必要がある場合
if X > 0 and 0 < Y < X and Z < 0:
    ans += abs(Z) * 2
elif X < 0 and X < Y < 0 and Z > 0:
    ans += abs(Z) * 2
print(ans)
