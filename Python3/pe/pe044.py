import time
from numba import jit


@jit(nopython = True)
def main2():
    p = [n * (3 * n - 1) // 2 for n in range(1, 2400)]
    for i in range(len(p)):
        for j in range(len(p)):
            chk1 = p[i] - p[j]
            if chk1 in p:
                chk2 = p[i] + p[j]
                if chk2 in p:
                    return chk1

def main1():
    pd = {}
    k = 1
    while(k < 2400):
        pk = k * (3 * k - 1) // 2
        pd[pk] = 1
        j = 1
        while(True):
            pj = 3 * j * k + j * (3 * j - 1) // 2
            if pj > pk:
                break
            if pj in pd and pk - pj in pd:
                return pk - pj
            j += 1
        k += 1


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


time_start = time.perf_counter()
print(main1())
lap()
# 5482660
# 0.31844/s

print(main2())
lap()
# 5482660
# 5.01400/s

# https://projecteuler.net/problem=44