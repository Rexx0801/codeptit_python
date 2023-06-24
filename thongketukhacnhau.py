import re
from collections import Counter

s = ""
for _ in range(int(input())):
    s += (input() + " ")

myList = sorted(re.findall("\\w+", s.lower()))

for k, v in sorted(Counter(myList).items(), key=lambda i: i[1], reverse=True):
    print(k, v)