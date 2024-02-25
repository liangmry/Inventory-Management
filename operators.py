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

# 产品类
class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def add_product(self, table):
        sql = f'insert into {table} values(%s, %s, %s, %s)'
        cursor.execute(sql, (self.product_id, self.name, self.description, self.price))
        # 提交更改
        conn.commit()

# # 库存类
# class Inventory:
#     def __init__(self):
#         self.products = []
#
#

p1 = Product('123', 'apple', 'ashda', 12.3)
p1.add_product('products')

# 关闭连接
cursor.close()
conn.close()