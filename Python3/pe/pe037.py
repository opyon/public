import re
from numba import jit


@jit(nopython = True)
def eratosthenes_list(n):
    primes = [True] * n
    result = [2]
    for prime in range(3, n, 2):
        if primes[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                primes[i] = False
    return result


def regular_chk(ps):
    reg = re.compile('^\d+[37]$')
    return re.match(reg, ps)


def is_truncatable_prime(s):
    s_len = len(s)
    for i in range(1, s_len):
        chk_L = int(s[i:])
        chk_R = int(s[:-i])
        if chk_L not in primes or chk_R not in primes:
            return False
    return True


def main1():
    result = []
    for prime in primes:
        ps = str(prime)
        if regular_chk(ps) and is_truncatable_prime(ps):
            result.append(prime)
        if len(result) == 11:
            print(result)
            break

    # 2+3+5+7=17
    return sum(result)


N = 10 ** 6
primes = eratosthenes_list(N)
print(main1())
# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# 748317
# https://projecteuler.net/problem=37
