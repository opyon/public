def main1():
    r = 0
    for i in range(1,1001):
        r += i ** i
    return str(r)[-10:]
def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1())
lap()
# 9110846700
# 0.00920/s
# https://projecteuler.net/problem=48