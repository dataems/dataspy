#coding=utf-8
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

#step1:建立类ScrawlFile(link,postfix,localpath)
#爬取指定链接link下的所有后缀postfix为数据文件，并保存到本地为localpath下

#step2:将下载的xls格式数据，转换成csv格式。
#时间序列户数据按条横向存储的
#CSV一条数据格式：带表头，时间（标准英文时间格式）,字段1,字段2,字段3,字段4


import datetime
import urllib
import re
import os
import xlrd
from bs4 import BeautifulSoup
from scrawl import save2mysql


class ScrawlFile:
    '''A Member object represents any other object being a 'member' of a
    particular Group.

    Meanings:
    * url - 
    * postfix - 
    * localpath - 
    '''
    
    def __init__(self,url,prefix,localpath):
        self.url = url
        self.prefix = prefix
        self.localpath = localpath

    def geturl(self):
        return self.url

    def fileretrievel(self):
        urllib.urlretrieve(self.url,self.localpath)
        urllib.urlcleanup() 
        print("done")

    def geturlfilelinks(self):
        #读取给定链接
        html = urllib.urlopen(self.url).read().decode("gb2312")
        #print  html

        #调用BeautifulSoup
        soup = BeautifulSoup(html,"lxml")

        #通过正则表达式过滤出要提取的链接
        #content = soup.findAll(class_ = 'gjzz_nr_lb')   
        #content = soup.findAll('a')  
        #content = soup.findAll('a',re.compile("[tongjxinxi]"))  #错误写法
        #content = soup.findAll('div', attrs={"class": "gjzz_nr_lb"})
        #content = soup.findAll('a', attrs={"title":re.compile("[201]")}) #正确写法 
        #content = soup.findAll('a', attrs={"href":re.compile(r'^http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/')}) #成功但多了3个链接
        content = soup.findAll('a', attrs={"title":re.compile("[\u4e00-\u9fa5][20]")})  #中文正则 [\u4e00-\u9fa5] 

        #print len(content)
       
        #完善链接格式
        pat = re.compile(r'href="([^"]*)"')
        pat2 = re.compile(r'http')

        for item in content:
            #print item.text
            h = pat.search(str(item))
            href = h.group(1)
            if pat2.search(href):
                ans = href
            else:
                ans = url+href
            #print(ans)
            #print self.getdownloadurl(ans)
            localfilename = os.path.join(self.localpath,item.text+".xls")
            localcsv = os.path.join(self.localpath,item.text+".csv")
            #print localfilename 
            self.downloadfile(self.getdownloadurl(ans),localfilename.encode("gbk"))
            save2mysql.trans_xls_csv(localfilename,localcsv)

    def downloadfile(self,x_url,x_localpath):
        #从x_url中找到最终的下载地址
        #将文件下载到本地
        urllib.urlretrieve(x_url,x_localpath)
        urllib.urlcleanup() 
        #print("done")


    def getdownloadurl(self,x_url):
        html = urllib.urlopen(x_url).read().decode("gbk")
        #调用BeautifulSoup
        soup = BeautifulSoup(html,"lxml")
        #content = soup.findAll('a', attrs={"title":re.compile("[\u4e00-\u9fa5]")})  #中文正则 [\u4e00-\u9fa5]
        content = soup.findAll('a', attrs={"href":re.compile("xls")})  #含有xls
        if len(content):
            return self.geturlfromtaga(str(content[0]))
        else:
            print "warring: some url without xls"
            return None
        

    def geturlfromtaga(self,x_string):
        #print x_string
        pat = re.compile(r'href="([^"]*)"')
        pat2 = re.compile(r'http')
        pat3 = re.compile(r'/d/file/')
        h = pat.search(x_string)
        if h:
            href = h.group(1)
            if pat2.search(href):
                ans = href
            else:
                ans = re.sub(pat3,self.prefix,href)
            #print ans
            return ans
        else:
            print "error in geturlfromtaga"
            return None






















        
