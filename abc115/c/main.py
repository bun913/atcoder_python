# -*- coding: utf-8 -*-
"""
解く前のメモ

NからK本を選んで、それらの最大のhと最小のhの差が最小のものを出力する
普通に考えれば組み合わせを全て出せば良いのだけどNが10**5なので全探索は無理(み合わせが10**10程度になる)

ソートした配列のどこか隣り合ったK本の組み合わせが今回の飾り付けの対象になる
(だって差が小さいものだから、並び替えた配列だったら隣り合ったものしかありえない)
"""
N, K = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]
HD = sorted(H)

ans = float('inf')

for i in range(N):
    # i+K-1がインデックスオーバーしたら終了
    if i + K - 1 > N-1:
        print(ans)
        exit()
    dif = HD[i+K-1] - HD[i]
    ans = min(ans, dif)
