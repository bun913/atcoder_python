# -*- coding: utf-8 -*-
"""
長さNの正しいかっこ列を全て辞書順に出力する

まずNが奇数なら終了
実はNが20なので全列挙でも行けそうではある
正しいカッコ列の判定は?
常に何番目の文字においても(の出現回数が)の出現回数以上となっている状態かな

(を1,)を2として考えてNこまでの組み合わせを全て列挙する
"""
from itertools import permutations


def is_valid(S: str) -> bool:
    count1 = 0
    count2 = 0
    for s in S:
        if s == '1':
            count1 += 1
        else:
            count2 += 1
        if count2 > count1:
            return False
    return True


N = int(input())
if N % 2 == 1:
    print('')
    exit()

a = ['1' for _ in range(N // 2)]
b = ['2' for _ in range(N // 2)]
a.extend(b)
cands = list(permutations(a, N))

ans_set = set()
for t in cands:
    S = ''.join(list(t))
    if is_valid(S) is False:
        continue
    ans_set.add(S)

ansers = sorted(list(ans_set))

for S in ansers:
    ans = S.replace('1', '(')
    ans = ans.replace('2', ')')
    print(ans)
