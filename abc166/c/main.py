# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
# 道の交わりを管理する辞書
ins_dic = dict([(i, []) for i in range(N)])

# 展望台の繋がりをメモしていく
for i in range(M):
    A, B = list(map(int, input().split()))
    A -= 1
    B -= 1
    ins_dic[A].append(B)
    ins_dic[B].append(A)

# 良い展望台、悪い展望台を管理する
ans = 0
ans_dic = dict((i, -1) for i in range(N))

for i in range(N):
    obse = i
    others = ins_dic[i]
    # 既に悪いと答えが出ている場合
    if ans_dic[i] == 0:
        continue
    # どことも繋がっていない
    if len(others) == 0:
        ans += 1
        ans_dic[i] = 1
        continue
    # 繋がっていて自分が最長か
    ownh = H[i]
    maxh = ownh
    maxob = i
    for other in others:
        otherh = H[other]
        # 他の展望台が高ければ自信を0にする(悪いにする)
        if max(maxh, otherh) == otherh:
            maxh = otherh
            maxob = other
    # 自分が最大かチェック
    if maxob == obse:
        ans += 1
        ans_dic[i] = 1
        # 他の展望台を悪いにマーク
        for other in others:
            ans_dic[other] = 0
print(ans)
