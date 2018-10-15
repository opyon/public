def main1():
    Td = set()
    Pd = set()
    Hd = set()

    n = 2
    while(True):
        tn = n * (n + 1) // 2
        Td.add(tn)
        Pd.add(n * (3 * n - 1) // 2)
        Hd.add(n * (2 * n - 1))
        if tn in Pd and tn in Hd:
            if n > 285:
                return tn
        n += 1


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1())
lap()
# 1533776805
# 0.05459/s
# https://projecteuler.net/problem=45