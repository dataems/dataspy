from scrawl import scrawlfile
from scrawl import save2mysql

url=['http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_2.html',
'http://www.cec.org.cn/guihuayutongji/tongjxinxi/yuedushuju/index_3.html']

for item in url:
    x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","E:\\down\\")
    #x=scrawlfile.ScrawlFile(item,"http://www.cec.org.cn/d/file/","/home/lican/Downloads/")
    x.geturlfilelinks()

#save2mysql.trans_xls_csv("E:\\down\\2011��1-4��ȫ��������ҵͳ������һ����.xls","E:\\down\\2011��1-4��ȫ��������ҵͳ������һ����.csv")



