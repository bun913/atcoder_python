# -*- coding: utf-8 -*-
"""
解く前のメモ

アナグラムの判定自体は文字列を sortしておえけばそんなに難しくない
Nが10**5なのでループは1回自体で決めないといけない
普通にsortした文字列をkeyにしてdictにメモしておけば良さそうだが
sort自体はlogNで実装されているはずなので間に合いそう

求めるのはアナグラムになるi,jの組み合わせの数という点に注意
"""

N = int(input())
memo = {}


for i in range(N):
    s = input()
    _sorted = "".join(sorted(s))
    if _sorted in memo:
        memo[_sorted] += 1
        continue
    memo[_sorted] = 1

# 最後に2以上の要素をConbinationで組数を数えて足しあげる
ans = 0
for v in memo.values():
    if v <= 1:
        continue
    ans += (v * (v-1) // 2)
print(ans)
