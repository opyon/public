import math
from numba import jit


@jit(nopython = True)
def integer_right_triangles(N):

    # 固定値なので変数に代入しておく
    cos_rad90 = math.cos(math.radians(90))

    ans = 0
    count_max = 0
    N += 1
    # 周をLとしてc=L-(a-b)を生成するループ
    for L in range(1, N):
        count = 0
        for a in range(1, L):
            for b in range(1, L):

                # ループでL,a,bから生成したcと余弦定理で求めたcを判定
                # 同じなら正解としてカウント
                c = L - (a + b)
                chk = math.sqrt(a * a + b * b - (2 * a * b * (cos_rad90)))
                if c == chk:
                    count += 1

        # 解が多いもので更新
        if count_max < count:
            count_max = count
            ans = L

    print(ans, count_max // 2)
    return ans


N = 1000
print(integer_right_triangles(N))
# 840

# https://projecteuler.net/problem=39
# http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2039
# 3辺が全て整数の直角三角形
# 辺の長さが {a,b,c} と整数の3つ組である直角三角形を考え,
# その周囲の長さを p とする. p = 120のときには3つの解が存在する:
# {20,48,52}, {24,45,51}, {30,40,50}
# p ≤ 1000 のとき解の数が最大になる p はいくつか?
