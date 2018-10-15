import time
from itertools import permutations


def get_pandigitals(n):
    d = [i for i in range(0 , n + 1,)]
    return list(permutations(d))


def unpack_pd(num_tuple):
    pd = 0
    for n in num_tuple:
            pd = 10 * pd + n
    return pd


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


def chk(ntp, even, mps, dn):
    if ntp[0] != 0 and ntp[3] in even and ntp[5] == 5:
        for i in range(5):
            if unpack_pd(ntp[dn[i]:dn[i] + 3]) not in mps[i]:
                return 0
    else:
        return 0
    return 1


def main1():
    # 'mps' is multiple lists
    mps = [[i for i in range(1, 1000) if i % x == 0]  for x in [17, 13, 11, 7, 3]]
    # 'dn' is digit n
    dn = [7, 6, 5, 4, 2]
    even = [0, 2, 4, 6, 8]
    count = 0
    for ntp in get_pandigitals(9):
            if chk(ntp, even, mps, dn):
                count += unpack_pd(ntp)
    return count


time_start = time.perf_counter()
print(main1())
lap()
# 16695334890
# 1.52657/s
# https://projecteuler.net/problem=43

# (1 406357289)0
# (1 406 357289)1 %2
# (1 4 063 57289)2 %3
# (1 40 635 7289)3 %5
# (1 406 357 289)4 %7
# (1 4063 572 89)5 %11
# (1 40635 728 9)6 %13
# (1 406357 289)7 %17

# (1, 4, 0, 6, 3, 5, 7, 2, 8, 9)
# (1, 4, 3, 0, 9, 5, 2, 8, 6, 7)
# (1, 4, 6, 0, 3, 5, 7, 2, 8, 9)
# (4, 1, 0, 6, 3, 5, 7, 2, 8, 9)
# (4, 1, 3, 0, 9, 5, 2, 8, 6, 7)
# (4, 1, 6, 0, 3, 5, 7, 2, 8, 9)

# 毎回（３桁目が偶数and５桁目が5）を通ったもの全てに対して判定が行われるので
# ループ毎に割り切れるか計算していると計算量が多くて遅くなる
# 試行錯誤して最初にリストを作り（各３桁 in 各リスト）で判定させると速くなった
# 計算せず比較のみになったことで3倍以上速くなったと推測
# 3.96685/s
# ↓
# 1.18327/s
# ↓
# 1.52657/s
# 処理は変えず冗長になった複数行をfor文でまとめたり関数化すると少し遅くなった
