import pymysql

conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123',
    database='db9',
    charset='utf8'
)

cur=conn.cursor(cursor=pymysql.cursors.DictCursor)

cur.callproc('proc1',(3,10)) #set @_proc1_0=3;set @_proc1_1=10
# print(cur.fetchone())


cur.execute('select @_proc1_1;')
print(cur.fetchone())

cur.close()
conn.close()

