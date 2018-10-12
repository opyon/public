import math
ans = 0
i = 3
e = 10 ** 5
while (i < e):
    total = 0
    for x in str(i):
        total += math.factorial(int(x))
    if i == total:
        ans += i
    i += 1
print(ans)
# 40730
# https://projecteuler.net/problem=34