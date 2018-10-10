file_name_in = r'C:\workspace\tmp\names.txt'
with open(file_name_in, "r", encoding = "utf-8") as open_file:
    src = open_file.read()
ofset = ord('A') - 1
print(sum([i * x for i, x in enumerate([sum([ord(s) - ofset for s in name]) \
                                     for name in sorted(src.replace(r'"', '').split(","))], 1)]))

# 871198282
# https://projecteuler.net/problem=22
