"""
Xが非常に大きい数となるので全探索は無理
Xをlogの計算に落とし込んで2分探索でとく
"""
# 再帰関数の限界を上げる
import sys
sys.setrecursionlimit(10**9)

A, B, X = map(int, input().split())


def is_ok(mid: int) -> bool:
    cost = A * mid + B * len(str(mid))
    if cost <= X:
        return True
    return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        # print(ok, ng, mid)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(10**9+1, 0)
print(ans)
