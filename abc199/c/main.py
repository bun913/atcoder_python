"""
長さが2Nの文字列Sが来る
Q個のクエリが来る
Ti = 1の時,SのAi文字目とBi文字目を入れ替える
Ti = 2の時,Sの先頭N文字と末尾N文字を入れ替える
実際にクエリを処理すると、特にTi=2の時にTLEになる
とうことであらかじめ2次元配列で半分に分けたリストを用意しておく
とすれば、Ti = 2の時もその配列を入れ替えるだけでよい
"""
N = int(input())
S = input()
L = list(S)
Q = int(input())
# 半分に分けた2次元配列を用意する
L = [L[:N], L[N:]]
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 2:
        # O(1)で済む
        L[0], L[1] = L[1], L[0]
        continue
    # a,bがそれぞれどっちの配列にあるか考える
    i1 = 0 if a <= N else 1
    i2 = 0 if b <= N else 1
    # それぞれの配列のインデックスを求める
    j1 = a - 1 if a <= N else a - N - 1
    j2 = b - 1 if b <= N else b - N - 1
    L[i1][j1], L[i2][j2] = L[i2][j2], L[i1][j1]
ans = ''.join(L[0]) + ''.join(L[1])
print(ans)
