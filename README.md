# 大数据大作业

#### 介绍
本课题为信息爬取字数及可视化，利用爬虫技术爬取任一门户网站新闻栏目一定时间段内的新闻信息，保存为一个或多个文件并上传到Hadoop平台以本人学号命名的文件夹下；利用MapReduce框架编程完成字数统计；利用Echarts或其他可视化平台，使用四种不同可视化效果分别展示出现频次前5、前10、前20、前50的单词可视化效果网页。

#### 软件架构
     本课题中涉及到的主要技术有：
        MapReduce框架编程进行字数统计、
        Python编程使用selenium库爬取网站动态新闻、
        Python编程对文本分词处理、
        Python编程对词频排序、
        利用Echarts平台展示词语可视化效果网页。
     开发环境：Linux系统、Hadoop平台、Echarts平台、Python环境
     软件工具：Pycharm 、Anaconda 、VMware Workstation Pro


#### 安装教程

1.  拉取代码到本地，使用pycharm打开


#### 使用说明
 
 

> 视频讲解参考：https://www.bilibili.com/video/BV1Yg411x7db/

>  博客细节参考：https://blog.csdn.net/m0_59310933/article/details/131205216

##### 1、安装所需要的工具包，提示缺什么就安装什么，pip install  包名

##### 2、下载msedgedriver.exe这个很重要，我用的edge浏览器，所以下载的这个，其他浏览器同样要找适配的。

- 2.1、首先查看浏览器的版本


- 2.2、看到对应浏览器版本，选择下载。


- 然后要把压缩包解压出来得到msedgedriver.exe，文件名更改为MicrosoftWebDriver.exe。把它放入和你python解释器同级的文件夹中

##### 3、都安装完毕此时就可以正常使用了，注意在分词完毕后，是使用到了Hadoop平台，利用MapReduce框架编写java程序，打成jar包，运行可执行jar包得到统计词频的。考虑到适用性，这里加入了一个python脚本词频统计.py。可以利用它模拟执行jhadoop平台WordCount.jar程序功能。词频统计结果输出为out.txt,可在程序中自行修改输出名字，在词频排序程序中要注意用的文件是哪个，改为out.txt（你修改的）即可

##### 4、可视化部分要将自己的数据放入即可

注：（合集.txt为爬取新闻的综合，手动综合）



#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

