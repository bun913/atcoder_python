"""
cが2つでSが作れる
Sccという組みを最大で何個作れるか
"""
S, C = list(map(int, input().split()))
ans = 0

# まずSが1個でもある場合その数だけ作る
set_cnt = min(S, C // 2)
ans += set_cnt
S -= set_cnt
C -= 2 * set_cnt
if C < 2:
    print(ans)
    exit()
# あとはCを4個消費すれば1個Sが作れる
ans += C // 4
print(ans)
