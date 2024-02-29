#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File:中文分词.py
# @Software:PyCharm
import jieba
import re
import cv2
import wordcloud

sf = "../停用词/停用词.txt"
f = open("合集.txt", "r", encoding="utf-8")
ls=jieba.lcut(f.read())
f.close()


stop_words = []
with open(sf,'r',encoding='utf-8') as f:
    for i in f.read().splitlines():
        stop_words.append(i)

la = re.sub(r'[\s\[|\]0123456789,、，。’+？！”“\']',"",str(ls))
txt0 =jieba.lcut(la)

#去除停用词
ans = []
for x in txt0:
    if x not in stop_words and len(x) > 1:
        ans.append(x)

res = " ".join(ans)
with open('../分词结果/a1.txt', 'w', encoding='utf-8') as fi:
    fi.write(res)
print(res)

mk = cv2.imread('mask.jpg')
wd = wordcloud.WordCloud(font_path='C:\Windows\Fonts\simkai.ttf',width=1800,height=1800,background_color='white',
                         mask=mk,stopwords=['要求','甚至','此次','虽然','发现','继续','一个']).generate(res)
wd.to_file('新闻1.png')

