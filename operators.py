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

# 产品表
table1 = 'products'

# 产品类
class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    # 添加产品
    def add_product(self):
        sql = f'insert into {table1} values(%s, %s, %s, %s)'
        cursor.execute(sql, (self.product_id, self.name, self.description, self.price))
        # 提交更改
        conn.commit()

    # 删除产品  提供根据id和name进行某一行的删除操作
    def delete_product_fromID(self):
        sql = f'delete from {table1} where product_id = {self.product_id}'
        cursor.execute(sql)
        conn.commit()

    def delete_product_fromNAME(self):
        sql = f'delete from {table1} where name = {self.name}'
        cursor.execute(sql)
        conn.commit()

    # 修改定价 id / name
    def modify_price_fromID(self, new_price):
        sql = f'update {table1} set price = {new_price} where product_id = {self.product_id}'
        cursor.execute(sql)
        conn.commit()

    def modify_price_fromNAME(self, new_price):
        sql = f'update {table1} set price = {new_price} where name = {self.name}'
        cursor.execute(sql)
        conn.commit()

    # 获取产品信息
    def show_product_info(self):
        sql = f'select price from {table1} where product_id = {self.product_id}'
        cursor.execute(sql)
        result_price = cursor.fetchall()

        sql2 = f'select name from {table1} where product_id = {self.product_id}'
        cursor.execute(sql2)
        result_name = cursor.fetchall()

        sql3 = f'select description from {table1} where product_id = {self.product_id}'
        cursor.execute(sql3)
        result_desc = cursor.fetchall()
        # 输出信息
        print(f'{self.product_id}：{result_name}的价格是{result_price}，它的基础信息是{result_desc}')


p1 = Product('123', 'apple', 'ashda', 12.3)
p1.add_product()
p1.show_product_info()
p1.modify_price_fromID(15.5)
p1.show_product_info()

# 关闭连接
cursor.close()
conn.close()