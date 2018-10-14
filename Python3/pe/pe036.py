# 回文数の生成
# http://d.hatena.ne.jp/inamori/20091216/p1
def gen_palindromic(k, B, l = 0):
    if l == k:
        yield 0
    elif l == k - 1:
        for d in range(B):
            yield d
    else:
        begin = 1 if l == 0 else 0
        m = B ** (k - l - 1) + 1
        for d in range(begin, B):
            for n in gen_palindromic(k, B, l + 2):
                yield n * B + d * m

count = 0
for i in range(1,7):
    for x in gen_palindromic(i,10):
        s = bin(x).replace('0b','')
        r = s[::-1]
        if s == r:
            count += x
print(count)
# 872187
# https://projecteuler.net/problem=36
