"""
Atcoderの問題解く用
"""
from math import sqrt, ceil

R, X, Y = list(map(int, input().split()))
abs_dis = sqrt(X**2 + Y**2)
ans = ceil(abs_dis / R)
# コーナーケース
if ans == 1 and abs_dis != R:
    ans += 1
print(ans)
