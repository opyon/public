import timeit
import itertools


def f1():
    n = set([i for i in range(10)])
    a = list(itertools.permutations(n))[1000000 - 1]
    print(a)
    b = list(map(str, a))
    print(b)
    print(''.join(b))


def f2():
    print(''.join(list(map(str, list(itertools.permutations(set([i for i in range(10)])))[1000000 - 1]))))

# (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
# ['2', '7', '8', '3', '9', '1', '5', '4', '6', '0']

print(timeit.timeit(lambda: f1(), number = 1))
# 2783915460
# 0.501804581

print(timeit.timeit(lambda: f2(), number = 1))
# 2783915460
# 0.48594570599999987

# https://projecteuler.net/problem=24