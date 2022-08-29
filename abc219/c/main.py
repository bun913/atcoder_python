"""
Atcoderの問題解く用

各文字列について、元のアルファベットでいう○に変換してやればよいのでは？
最大で５万の文字で、文字長が10だからなんとかなりそう
"""


def num2alpha(num):
    if num <= 26:
        return chr(64+num)
    elif num % 26 == 0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num % 26)


X = input()
N = int(input())
memo = {}
r_memo = {}

# 今の文字をメモ化
for i in range(1, 27):
    org = num2alpha(i)
    new = X[i-1]
    memo[new] = org
    r_memo[org] = new


# 名前を本来のアルファベットの文字列として置換してメモ
replaces_list = []
for i in range(N):
    replaced = []
    S = input()
    for s in S:
        replaced.append(memo[s])
    replaces_list.append(''.join(replaced))

# ソートしてまた戻すだけ
replaces_sorted = sorted(replaces_list)

for S in replaces_sorted:
    re_converted = []
    for s in S:
        re_converted.append(r_memo[s])
    print(''.join(re_converted))
