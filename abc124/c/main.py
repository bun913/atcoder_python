# -*- coding: utf-8 -*-
"""
解く前のメモ

最初の色は0,または1であり、全ての隣り合うタイルも異なる色で塗られるようにしたい
つまり理想とする色の塗り方は
1,0,1,0...
0,1,0,1...
の2パターンしかないので、両方やって塗り替える数が少ない方を使えば良いだけでは
"""
S = input()

start0 = 0
cur_color = '0'

for s in S:
    if s != cur_color:
        start0 += 1
    # 次のタイルの理想の色へ合わせる
    if cur_color == '0':
        cur_color = '1'
        continue
    cur_color = '0'

start1 = 0
cur_color = '1'

for s in S:
    if s != cur_color:
        start1 += 1
    # 次のタイルの理想の色へ合わせる
    if cur_color == '0':
        cur_color = '1'
        continue
    cur_color = '0'

print(min(start0, start1))
