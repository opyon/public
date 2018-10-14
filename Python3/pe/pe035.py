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
    reg = re.compile('^[1379]+$')
    return re.match(reg, ps)


def is_circular_primes(ps):
    ps_len = len(ps)
    for _ in range(ps_len - 1):
        ps = ps[1:] + ps[:1]
        if int(ps) not in primes:
            return False
    return True


def main1():
    count = 0
    for prime in primes:
        if prime in [2, 3, 5, 7]:
            count += 1
            continue

        #ps is prime strings
        ps = str(prime)
        if regular_chk(ps):
            if is_circular_primes(ps):
                count += 1
    return count


N = 10 ** 6
primes = eratosthenes_list(N)
print(main1())
# N = 10 ** 6
# 55
# https://projecteuler.net/problem=35

primes = eratosthenes_list(100)
assert (main1() == 13)


