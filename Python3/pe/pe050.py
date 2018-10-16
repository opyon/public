from numba import jit


@jit(nopython = True)
def get_primes_list(n):
    sieve = [1] * n
    result = [2]
    for prime in range(3, n, 2):
        if sieve[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                sieve[i] = 0
    return result


@jit(nopython = True)
def main1(N):
    primes = get_primes_list(N)
    limit = len(primes)
    e = limit
    while(e>1):
        chk_len = limit - e
        for i in range(0,chk_len+1):
            chk = 0
            ie = i+e
            for j in range(i,ie):
                chk += primes[j]
            if chk > N:
                break
            if chk in primes:
                return chk
        e -= 1


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1(1000000))
lap()
# 997651
# 2.57364/s
# https://projecteuler.net/problem=50
# 概要
# 素数リストの最大長のsum()から
# 最大長-1づつのループでsum()を求め素数判定
# startとendをループでずらす例
# リスト　123456789
# 最大長　3
# ループ　1:123,2:234,3:345,,,
# sum()が使えないのでforで書き直し


# 以下最初に作った遅かったもの
# 19.44282/s
@jit(nopython=True)
def main2(N):
    primes = get_primes_list(N)
    limit = len(primes)
    i = 2
    ans = 0
    count_max = 0
    while(i < limit):
        tmp = 0
        count = 0
        for j in range(i,limit):
            tmp += primes[j]
            if tmp > N:
                break
            count += 1
            if tmp in primes:
                if count_max < count:
                    count_max = count
                    ans = tmp
        i += 1
    return ans
time_start = time.perf_counter()
print(main2(1000000))
lap()
# 19.44282/s