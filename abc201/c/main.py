"""
答えがたかだか10の4乗なので全て数え上げれば良い
"""
S = input()
must_inc = set()
not_inc = set()
all_cands = [str(i) for i in range(10)]
for i, s in enumerate(S):
    if s == "o":
        must_inc.add(str(i))
    elif s == "x":
        not_inc.add(str(i))
ans_set = set()
for a in all_cands:
    for b in all_cands:
        for c in all_cands:
            for d in all_cands:
                cand = a + b + c + d
                # 含んではいけない文字を含んでいる場合
                should_skip = False
                for s in cand:
                    if s in not_inc:
                        should_skip = True
                        break
                if should_skip is True:
                    continue
                if len(set(cand).intersection(must_inc)) == len(must_inc):
                    ans_set.add(cand)
print(len(ans_set))
