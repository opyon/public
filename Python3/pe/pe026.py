from decimal import *
import re

getcontext().prec = 2000
max_len = {}

for i in range(3,1000,2):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
        continue
    else:
        str_num = re.sub(r'^0\.0*'  , "", str(Decimal(1)/Decimal(i)))
        j = 0
        while(True):
            j += 1
            if str_num[:j] == str_num[j:j*2]:
                max_len[i]=j
                break

print(max(max_len, key=max_len.get))
