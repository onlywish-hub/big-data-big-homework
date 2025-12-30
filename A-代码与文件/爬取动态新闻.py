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
    print("时间到，开始运行~")
    browser = webdriver.Edge()
    browser.get('https://www.ifeng.com')
    browser.implicitly_wait(1800)  # 默认300秒
    page_text = browser.page_source
    tree = etree.HTML(page_text)

    # 原来精度过深，导致路径不具有普适性 li_list = tree.xpath('//*[@id="root"]/div/div[6]/div[2]/div[2]/div[2]')
    # 修改后：下面注释掉的可以获取页面所有新闻文本
    # li_list = tree.xpath('//div[contains(@class, "news_list")] | //div[contains(@class, "index_news_list")]')
    # 下面是获取中间一栏新闻文本，可以选择left,center,right进行切换
    li_list = tree.xpath('//div[contains(@class, "center_box")]')
    fo = open('../爬取新闻结果/XinWen{}.txt'.format(v), 'w', encoding='utf-8')
    ls = []
    for li in li_list:
        # 若要获取第一个list，可以使用下标指定li_list[0]
        # 只要 p 标签类名包含 news_list 就行能获取所有
        # con = li.xpath('.//p[contains(@class, "news_list")]/a/@href')
        # 获取具体一个方框内的文本，可以在详细一点路径
        # con = li.xpath('.//p[contains(@class, "news_list_p_5zOEF")]/a/@href')
        con = li.xpath('.//p[contains(@class, "news_list")]/a/@href')
        print(len(con),"条新闻")
        for i in range(len(con)):
            htt = "" + con[i]
            browser.get(htt)
            browser.implicitly_wait(10)  # 确保元素有时间加载
            text = browser.page_source
            ee = etree.HTML(text)
            # lis = ee.xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div[1]')
            # 上面这个是原来的，精细控制，但是不具备普适性，下面已进行修改
            lis = ee.xpath('//div[contains(@class, "main_content")]')
            for j in lis:
                ls.append(j.xpath('.//p/text()'))
        print(con)
        print(ls)
    ans = ''
    ans += str(ls)
    fo.write(ans)
    fo.close()
    sleep(5)
    browser.quit()


def main():     #建议将 h 设置为0或6或12或18 获取新闻文本几乎不会重复
    print("开始准备爬取了，等待时间到达指定时间~~~")
    ################## 爬取前首先自己修改下时间 ####################
    h = 16     # 设置开始爬取的小时
    m = 18     # 设置开始爬取的分钟
    v = 14  # 设置文件名后缀起始编号，0
    ############################################################
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
