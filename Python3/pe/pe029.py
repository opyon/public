s = set()
for i in range(2,101):
    for j in range(2,101):
        s.add(i**j)
        s.add(j**i)
print(len(s))
# 9183
# https://projecteuler.net/problem=29