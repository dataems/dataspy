#encoding=utf-8
import sys
import MySQLdb

#读取本地的.xls文件，转换成csv格式的数据，时间序列按条存储的格式
#CSV一条数据格式：带表头，时间（标准英文时间格式）,字段1,字段2,字段3,字段4

reload(sys)
sys.setdefaultencoding('utf-8')


db=MySQLdb.connect(host='localhost', user='lican', passwd='abcd1234',charset='utf8')
cur=db.cursor()
cur.execute('use data_ems')
cur.execute('select * from geo limit 100')

#f=file("e:\\down\\tes.txt",'w')
f=file("/home/lican/Downloads/test.txt","w")


for i in cur.fetchall():
    f.write(str(i))
    f.write("\n")

f.close()
cur.close()
