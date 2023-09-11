# -*- coding: utf-8 -*-
"""
"""
N, Q = map(int, input().split())
num_inds = dict([(i, i) for i in range(1, N+1)])
ind_nums = dict([(i, i) for i in range(1, N+1)])

for _ in range(Q):
    left_num = int(input())
    left_ind = num_inds[left_num]
    # left_indがNの時だけright_indはleft_indの横の数字になる
    right_ind = left_ind + 1 if left_ind < N else left_ind - 1
    right_num = ind_nums[right_ind]
    # 更新する
    num_inds[left_num], num_inds[right_num] = right_ind, left_ind
    ind_nums[left_ind], ind_nums[right_ind] = right_num, left_num

# 答えを出力
ans = []
for ind, num in sorted(ind_nums.items()):
    ans.append(str(num))
print(*ans)
