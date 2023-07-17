"""
整数Nをどっかで分割して、好きに並べ替える
分割後の数の積の最大値を求める
bit全探索で使う数を決めようか、たかだか10桁だし
であとはソートして使えばOK
ただし0始りの数は許されないことに注意
"""
from itertools import product


def can_convert(str_list):
    if str_list[0] == '0' and len(str_list) > 1:
        return False
    return True


N = input()
L = list(N)

ans = -1
for bits in product([True, False], repeat=len(N)):
    # 全部Trueと全部Falseは飛ばす
    left = []
    right = []
    for i, is_left in enumerate(bits):
        if is_left is True:
            left.append(L[i])
            continue
        right.append(L[i])
    if len(left) == 0 or len(right) == 0:
        continue
    left_sorted = sorted(left, reverse=True)
    right_sorted = sorted(right, reverse=True)
    # 0始まりの場合はスキップ
    if can_convert(left_sorted) is False:
        continue
    if can_convert(right_sorted) is False:
        continue
    left_num = int(''.join(left_sorted))
    right_num = int(''.join(right_sorted))
    ans = max(ans, left_num * right_num)
print(ans)
