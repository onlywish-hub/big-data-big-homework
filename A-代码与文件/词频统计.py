#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File: 词频统计.py 

try:
    with open('../分词结果/a1.txt', 'r', encoding='utf-8') as f:
        lines = f.read().split()
    dic = {}
    for w in lines:
        dic[w] = dic.get(w, 0) + 1
    ls = list(dic.items())
    ls.sort(key=lambda x: x[0])
    with open('../词频统计结果/out.txt', 'w', encoding='utf-8') as f:
        for i in range(len(ls)):
            f.write('{} {}\n'.format(ls[i][0], ls[i][1]))
    print("词频统计完成，结果已保存至 out.txt")
except Exception as e:
    print(f"发生错误：{e}")