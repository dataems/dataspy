#月度数据爬取逻辑
#从中电联网站上抓取每月发布的excel数据文件，将数据文件按照月份存入mysql库
#查看数据库中已有的最新月份，爬取从最后爬取月到当前月的数据。
#如果数据库中没有任何一个月的数据，则爬取网站上已有所有月份的数据
#爬取的数据文件按照月份重新命名
#中电联网站的月度数据的网址是（该链接下的所有xls文件）
#http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/

#年度数据爬取逻辑
#中电联网站的年度数据的网址是（该链接下的所有xls文件）
#http://www.cec.org.cn/guihuayutongji/tongjxinxi/niandushuju/
#该链接下的所有xls文件，按照年份存入mysql库
#如果数据库中没有任何一个年份的数据，则爬取所有的年份数据
#如果以有某些年的数据，则取最新的年份，爬取最新年份与当前年份之间的数据

#step1:建立函数crawlFile(link,postfix,localpath)
#爬取指定链接link下的所有后缀postfix为数据文件，并保存到本地为localpath下

import datetime

class ScrawlFile:
    '''A Member object represents any other object being a 'member' of a
    particular Group.

    Meanings:
    * link - 
    * postfix - 
    * localpath - 
    '''
    
    def __init__(self,link,postfix,localpath):
        self.link = link
        self.postfix = postfix
        self.localpath = localpath

    def fib3(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while b < n:
            print(b)
            a, b = b, a+b
        print()


    def secondvalue(e):
        g = e
        print(g)
