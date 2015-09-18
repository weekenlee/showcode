# coding: utf-8
f = open("tx")
s = f.read()
s = s.replace('\n',' ')
words = s.split()
from collections import Counter
print dict(Counter(words))
