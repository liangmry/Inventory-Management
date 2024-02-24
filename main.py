import mysql.connector

# 建立数据库连接
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='test'
)
# 获取游标对象
cursor = conn.cursor()

# 操作
cursor.execute('show tables;')

result = cursor.fetchall()

print(result)

# 关闭连接
cursor.close()
conn.close()