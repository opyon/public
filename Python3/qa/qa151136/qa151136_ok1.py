import sys
import math
import threading
# 再帰回数の上限
# sys.setrecursionlimit(2100000000)
sys.setrecursionlimit(10000)

#@hayataka2049さん回答より追加
threading.stack_size(128*1024*1024)

def fibo2(n_1, n_2, count):
    n = n_1 + n_2
    count += 1
    if n >= target:
        return count
    return fibo2(n, n_1, count)

# N = 1000で問題を解きたいのに
# N = 823以上になると結果が表示されなかった
# N = 823
def main1():
    N = 1000
    global target
    target = 10 ** (N-1)
    print(fibo2(1, 1, 2))

target = 0
# @hayataka2049さん回答より追加
threading.Thread(target=main1).start()