# -*- coding: utf-8 -*-
"""
友人関係ごとにグループを作って、最大の人数となるグループの人数が答え
つまり隣接成分の最大の大きさとなるかな
幅優先探索とかで答えを求めることはできるものの、NMが大きいのでTLEになる
ノードの関係を整理するのに便利なのがUnionFind
グループのリーダーを決めてしまい、リーダーが一致するかどうかが同一グループに所属しているか確認する
Unionはグループの統合、Findはリーダーの確認
グループ同士を統合するときも同様にリーダーを確認する
人数が少ない方のグループ所属者を全て人数が多い方のグループのリーダーの子分にする
グループの統合をO(logN)でする。
"""
from functools import reduce

# UnionFind


class UnionFind:
    # 初期化 nは要素数
    def __init__(self, n):
        # 全体の大きさ
        self.n = n
        # -x:グループのサイズ(自身が根),k(正):根がk
        self.parent_size = [-1]*n

    # 要素の根を返す
    def leader(self, a):
        # aが根ならa自身を返す
        if self.parent_size[a] < 0:
            return a
        # aが根でないなら根に向かって木をたどる＋根の更新
        self.parent_size[a] = self.leader(self.parent_size[a])
        # 根を返す
        return self.parent_size[a]

    # aとbを結合
    def merge(self, a, b):
        # a,bの根をx,yへ
        x, y = self.leader(a), self.leader(b)
        # 根が同じなら終了
        if x == y:
            return
        # グループのサイズ=要素数を比較　サイズの小さい方を大きい方につなげるため
        # x<yならばx,yを入れ替える
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        # サイズの更新：小さい方のサイズを大きい方のサイズに足す
        self.parent_size[x] += self.parent_size[y]
        # サイズが小さい方の根を大きい方の根につなげる
        self.parent_size[y] = x
        return

    # 同じグループか判定　同じならTrue
    def same(self, a, b):
        # 根を比較して同じならTrue
        return self.leader(a) == self.leader(b)

    # 属するグループのサイズを返す
    def size(self, a):
        # 根の絶対値=サイズ
        return abs(self.parent_size[self.leader(a)])

    # groupの全体を返す
    def groups(self):
        # グループの格納リストを作る
        result = [[] for _ in range(self.n)]
        # リストの生成
        for i in range(self.n):
            result[self.leader(i)].append(i)
        # 空の要素を消す
        return [r for r in result if r != []]


N, M = map(int, input().split())
uni = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    # A,Bが友達関係であることを記録
    uni.merge(A-1, B-1)
friends_group = uni.groups()
# 最も人数の大きいグループのサイズを出す
ans = reduce(lambda x, y: max(x, y), map(len, friends_group))
print(ans)
