from numba import jit
import itertools as it
import math
import timeit


@jit(nopython = True)
def is_abundant1(n):
    len_n = n // 2 + 1
    total = 1
    for i in range(2, len_n):
        if n % i == 0:
            total += i
    return total > n


@jit(nopython = True)
def abundants1(N):
    result = set()
    for i in range(1, N):
        if i not in result and is_abundant1(i):
            for j in range(i, N, i):
                result.add(j)
    return result


@jit(nopython = True)
def is_abundant2(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    total = 0
    for i in set(divs):
        total += i
    return total > n


@jit(nopython = True)
def abundants2(N):
    result = set()
    for i in range(1, N):
        if i not in result and is_abundant2(i):
            for j in range(i, N, i):
                result.add(j)
    return result


def main1():
    NN = 28123
    abundants_set = abundants1(NN)
    abundants_product = set(map(sum, it.product(abundants_set, abundants_set)))
    numbers = set(range(1, NN + 1))
    print(sum(numbers - abundants_product))


def main2():
    NN = 28123
    abundants_set = abundants2(NN)
    abundants_product = set(map(sum, it.product(abundants_set, abundants_set)))
    numbers = set(range(1, NN + 1))
    print(sum(numbers - abundants_product))


print(timeit.timeit(lambda: main1(), number = 1))
# 6.77530854

print(timeit.timeit(lambda: main2(), number = 1))
# 5.589081999

# 4179871
# https://projecteuler.net/problem=23

# for i in range(1,100):
#     print(i,is_abundant2(i))
