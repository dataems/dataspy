#coding=utf8
from scrawl import scrawlfile
from scrawl import save2mysql

url=['http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_2.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_3.html']

for item in url:
    x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","E:\\down\\")
    #x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","/home/lican/Downloads/")
    x.geturlfilelinks()

#save2mysql.trans_xls_csv("E:\\down\\2011年1-4月全国电力工业统计数据一览表.xls","E:\\down\\2011年1-4月全国电力工业统计数据一览表.csv")



