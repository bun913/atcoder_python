# -*- coding: utf-8 -*-
"""
400で割った時の商でレートを決めることができそう
3200以上は最後にまとめて計算するのが良さそう
3200以上は書いてある色以外も選ぶことができるとのこと
"""
N = int(input())
A = list(map(int, input().split()))

below_reds = list(filter(lambda x: x <= 3199, A))
over_reds = list(filter(lambda x: x > 3199, A))

min_set = set()
# 好きな色を選ぶことは考えない
for r in below_reds:
    c = r // 400
    min_set.add(c)
# 3200以上で好きに選ぶ
min_ans = len(min_set)
max_ans = min_ans
for r in over_reds:
    # 3199以下が一人もいない場合時だけ最小値を増加させる
    if min_ans == 0:
        min_ans += 1
    max_ans += 1
print(min_ans, max_ans)
