from scrawl import scrawlfile
#scrawlfile.fib(1000)
#scrawlfile.ScrawlFile.fib3(1000)
#url='http://www.cec.org.cn/d/file/guihuayutongji/tongjxinxi/yuedushuju/2015-09-18/63b70681e81a2747dbd8f9d15228285f.xls'
url=['http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_2.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_3.html']
for item in url:
    #x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","E:\\down\")
    x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","/home/lican/Downloads/")
    x.geturlfilelinks()
