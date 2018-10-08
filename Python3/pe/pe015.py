import math


def lattice_paths(n):
    return math.factorial(n * 2) // math.factorial(n) ** 2


print(lattice_paths(20))
# 137846528820

# https://projecteuler.net/problem=15