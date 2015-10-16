from scrawl import scrawlfile
import xlrd
#scrawlfile.fib(1000)
#scrawlfile.ScrawlFile.fib3(1000)
#url='http://www.cec.org.cn/d/file/guihuayutongji/tongjxinxi/yuedushuju/2015-09-18/63b70681e81a2747dbd8f9d15228285f.xls'
'''
url=['http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_2.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_3.html']
for item in url:
    x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","E:\\down\\")
    #x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","/home/lican/Downloads/")
    x.geturlfilelinks()
'''


xlrd.biffh.unpack_unicode.func_globals["unicode"] = lambda s, e: unicode(s, e, errors="ignore") 
book = xlrd.open_workbook("e:\\down\\2009年1-8月全国电力工业统计数据一览表.xls", encoding_override="utf-8")
#book = xlrd.open_workbook("e:\\down\\test1.xls")
for sheet in book.sheet_names():
    print sheet

table = book.sheets()[0] #通过索引顺序获取
nrows = table.nrows 
ncols = table.ncols 

for i in range(nrows ):
    s=table.row_values(i)
    for item in s:
        if (type(item) == float ):
            print item
        else:
            print item.encode("gbk")
