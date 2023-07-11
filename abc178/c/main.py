"""
条件を全て満たす数を探るより、条件を満たさない数を探す方が早い
"""
N = int(input())
if N == 1:
    print(1)
    exit()
if N == 2:
    print(2)
    exit()
mod = 10 ** 9 + 7
alL_cnt = pow(10, N, mod)
# 0だけは存在しない配列の数
not_zero_cnt = pow(9, N, mod)
# 9だけは存在しない配列の数
not_nin_cnt = pow(9, N, mod)
# 0と9だけは存在しない配列の数
not_zero_nin_cnt = pow(8, N, mod)
ans = alL_cnt - not_zero_cnt - not_nin_cnt + not_zero_nin_cnt
print(ans)
