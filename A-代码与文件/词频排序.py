#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File:词频排序.py
# @Software:PyCharm

with open('../词频统计结果/out.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
dic = {}
for line in lines[:-1]:
    lk = line.strip("\n").split()
    dic[lk[0]] = dic.get(lk[0],int(lk[1]))
li = list(dic.items())
li.sort(key=lambda x:x[1],reverse=True)
print('词频前5：',li[:5])
print("-------------------------------------------------")
print('词频前10：',li[:10])
print("-------------------------------------------------")
print('词频前20：',li[:20])
print("-------------------------------------------------")
print('词频前50：',li[:50])

