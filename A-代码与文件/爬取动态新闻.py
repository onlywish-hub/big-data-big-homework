#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File:爬取动态新闻.py
# @Software:PyCharm
import requests
from lxml import etree
from selenium import webdriver
from time import sleep
import datetime
import time


def getCon(v):
    print("----------------------华丽的分割线----------------------")
    print("开始运行~")
    browser = webdriver.Edge()
    browser.get('https://www.ifeng.com')
    browser.implicitly_wait(1800)  # 默认300秒
    page_text = browser.page_source
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="root"]/div/div[6]/div[2]/div[2]/div[2]')

    fo = open('../爬取新闻结果/XinWen{}.txt'.format(v), 'w', encoding='utf-8')
    ls = []
    for li in li_list:
        # con = li.xpath('./p[@class="news_list_p-3EcL2Tvk "]/a/@href')
        # 上面这个是原来的，发现不能用了，只要修改这个 xpath 的路径就好。
        # con = li.xpath('./p[@class="index_news_list_p78SU "]/a/@href')  左边新闻备选
        con = li.xpath('./p[@class="index_news_list_p_5zOEF "]/a/@href')
        print(len(con),"条新闻")
        for i in range(len(con)):
            htt = "" + con[i]
            browser.get(htt)
            text = browser.page_source
            ee = etree.HTML(text)
            lis = ee.xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div[1]')
            for j in lis:
                ls.append(j.xpath('./p/text()'))
        print(con)
        print(ls)
    ans = ''
    ans += str(ls)
    fo.write(ans)
    fo.close()
    sleep(5)
    browser.quit()


def main():     #建议将 h 设置为0或6或12或18 获取新闻文本几乎不会重复
    h = 23
    m = 45
    v = 11  #文件名后缀起始编号，0
    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            v += 1  #生成文件名递增
            h += 6  #每隔多长时间爬取一次
            h %= 24
            getCon(v)
            print("现在时间：{}".format(now))
            print("下一次爬取时间：{}时{}分".format(h,m))

            # 执行完休息60秒避免重复
            time.sleep(60)

        # 每隔60秒检测一次,不然会漏
        time.sleep(60)


if __name__ == '__main__':
    main()
    print("----测试分割线----")
