s = ''.join([str(i) for i in range(185186)])
total = 1
print(len(s))
for i in range(1, 7):
    x = 10 ** i
    total *= int(s[x:x + 1])
print(total)
# 210
# https://projecteuler.net/problem=40