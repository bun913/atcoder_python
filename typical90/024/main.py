# -*- coding: utf-8 -*-
"""
解く前のメモ

ちょうどK回の操作でAをBに一致させることあgできるか
- 1 <= i <= Nを満たすiを選び Ai を Ai-1 or Ai + 1に置き換える

Nがたかだか1000なのに対してKが10 **9となっている
操作をシュミレートするのは不可能

ただここで気になるのが、1大きくするか1小さくするかしかできないこと
これにより偶数・奇数が重要になってきそう

AもBもサイズが一緒なのでから、それぞれの差の絶対値をとっていく
それにより 絶対値の差の和が K以下かつ Kとの偶奇があっておけば一緒にできるのでは
"""

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

abs_sum = 0

for i in range(N):
    a = A[i]
    b = B[i]
    abs_sum += abs(a-b)

ans = 'No'
if abs_sum <= K and abs_sum % 2 == K % 2:
    ans = 'Yes'
print(ans)
