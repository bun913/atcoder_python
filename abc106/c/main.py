# -*- coding: utf-8 -*-
"""
5000兆日語と決まっている
2以上の5000兆乗は当然Kの限界である10**18より大きいはず
では最初の文字が1以上か2以上かで場合分けすれば良いのでは
"""
S = input()
K = int(input())

# 最初の文字列が1意外ならその数字で決まり
if not S.startswith("1"):
    print(S[0])
    exit()
# 1だけで構成されている場合1
if len(set(S)) == 1:
    print(1)
    exit()
# # SがK文字以下の場合
# if K <= len(S):
#     print(S[K - 1])
#     exit()
# 1から始まるけどそれ以降に2以上の文字が存在する
for i, s in enumerate(S):
    if i + 1 == K:
        print(s)
        exit()
    # K文字目以下で1以外の数字が見つかった場合
    if s != "1":
        print(s)
        exit()
