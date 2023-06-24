# -*- coding: utf-8 -*-
"""
解く前のメモ用
Nが10**5でかつせいぜい6桁くらいしかないので言われた通りにやっても間に合いそう
"""
N = int(input())
ans = 0
for i in range(1, N+1):
    oct_num = oct(i)
    oct_str = str(oct_num)[2:]
    str_num = str(i)
    if oct_str.find("7") == -1 and str_num.find("7") == -1:
        ans += 1
print(ans)
