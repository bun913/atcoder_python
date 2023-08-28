# -*- coding: utf-8 -*-
"""
雰囲気であるが大体3手以内で移動が終わりそうだなと
0手 → すでに同じ
1手 → 絶対距離が3以内 or 1回の斜め移動でいける
2手 → 絶対距離が6以内 or 2回の斜め移動でいける
"""


def can_move1(a, b, c, d):
    if abs(a-c) + abs(b-d) <= 3:
        return True
    if a + b == c + d or a-b == c-d:
        return True
    return False


a, b = map(int, input().split())
c, d = map(int, input().split())


# 0手
if a == c and b == d:
    print(0)
    exit()
# 1手
if can_move1(a, b, c, d):
    print(1)
    exit()
# 2手は一旦斜めは無視して絶対距離が3以内のますに移動を全部試す
# そこから1手で行ければOK
for x in range(-3, 4):
    for y in range(-3, 4):
        if abs(x) + abs(y) > 3:
            continue
        new_a = a + x
        new_b = b + y
        print((a, b), (new_a, new_b), (x, y))
        # print((new_a, new_b), (c, d))
        if can_move1(new_a, new_b, c, d):
            print(2)
            exit()
# 3手はそれ以外
print(3)
