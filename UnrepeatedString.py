"""对于一个字符串,请设计一个高效算法，找到字符串的最长无重复字符的子串长度。
给定一个字符串A及它的长度n，请返回它的最长无重复字符子串长度。保证A中字符全
部为小写英文字符，且长度小于等于500。"""

s = input()
ret = 0
one_max = 0
dict = {}
start = 0
length = len(s)
if length == 0 or s is None:
    print(ret)

for i in range(length):
    if s[i] in dict and dict[s[i]] >=start:
        start = dict[s[i]] + 1
    one_max = i - start + 1
    dict[s[i]] = i
    ret = max(ret, one_max)

print(ret)