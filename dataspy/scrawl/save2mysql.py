#encoding=utf-8
import sys
import MySQLdb

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
