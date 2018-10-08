def is_leap_year(y):
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        return True
    else:
        return False


def month_days(y, m):
    if m == 2:
        total_days = 28 + is_leap_year(y)
    elif m in (4, 6, 9, 11):
        total_days = 30
    else:
        total_days = 31
    return total_days


def counting_sundays(start_year, end_year):
    sundays = 0
    total_days = 0
    if end_year > 1900:
        total_days = 365
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            if (total_days + 1) % 7 == 0:
                sundays += 1
            total_days += month_days(y, m)
    return sundays


print(counting_sundays(1901, 2000))
# 171

# https://projecteuler.net/problem=19
# http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2019

# 次の情報が与えられている.
# 1900年1月1日は月曜日である.
# 9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
# 2月は28日まであるが, うるう年のときは29日である.
# うるう年は西暦が4で割り切れる年に起こる.
# しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
# 20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
