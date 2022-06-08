"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input() 
#int型で受け取るとき
s = int(input()) 
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""

"""
これらのサイトがわかりやすかった
http://zakii.la.coocan.jp/enumeration/30_capsuletoy.htm
https://doryokujin.hatenablog.jp/entry/2012/05/09/034209

小難しく考えているけど、例えば全て3種類のうちから 1=>2 種類目時点のことを考えよう
1 => 2種類になる確率は 2/3
で・・・この時 n回引いたら大体１個でるというのは・・・ n*2/3 = 1
つまり・・ n = 1 / 2/3 となり、 n = 1.5となる(2/3)
※ 難しく考えすぎ、確率がわかっていれば 1 / 確率　とすれば、期待される数がわかると言うだけのこと
※ あれ？ってなったら 確率 1/2 で期待される試行回数2をどう導いたか考えれば余裕

"""
n = int(input())
ans = 0
# i種類揃っている状態からi+1種類を揃える時点の期待値を求めれば良い
for i in range(n):
    # 確率
    e = (n-i) / n
    # 期待される回数
    ans += 1 / e
print(ans)
