import math
triangles = {1:1, 2:2}


def divisor(n):
    if n in triangles: return triangles[n]
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1
    count *= 2
    if n == sqrt_n * sqrt_n:
        count -= 1
    triangles[n] = count
    return count


def main(target):
    n = 0
    while(True):
        n += 1
        if n % 2 == 0:
            x = n // 2
            y = n + 1
        else:
            x = n
            y = (n + 1) // 2

        xx = divisor(x)
        yy = divisor(y)
        d = xx * yy
        t = x * y
        triangles[t] = d
        if d >= target:
            print('n:{} t:{} x:{} xx:{} y:{} yy:{} d:{}'.format(n,t,x,xx,y,yy,d))
            print(t)
            break


import timeit
print(timeit.timeit(lambda: main(500), number = 1))

# https://projecteuler.net/problem=12
# https://teratail.com/questions/141215
# 辞書追加後
# n:12375 t:76576500 x:12375 xx:24 y:6188 yy:24 d:576
# 76576500
# 0.045450949000000004

# 辞書追加前
# 76576500
# 0.0888838
