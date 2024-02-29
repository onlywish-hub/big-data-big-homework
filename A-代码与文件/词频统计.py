#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File: 词频统计.py 

with open('../分词结果/a1.txt', 'r', encoding='utf-8') as f:
    lines = f.read().split()
dic = {}
for w in lines:
    dic[w] = dic.get(w, 0) + 1
ls = list(dic.items())
ls.sort(key=lambda x:x[0])
f = open('../词频统计结果/out.txt', 'w', encoding='utf-8')
for i in range(len(ls)):
    f.write('{} {}\n'.format(ls[i][0],ls[i][1]))
f.close()