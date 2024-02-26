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
# 库存表
table2 = 'inventory'

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


# 库存类
class Inventory:
    # 创建仓库
    def __init__(self):
        self.my_inventory = {}

    # 产品入库，包括产品自身，入库号码，数量
    def add_product(self, product, inventory_id, quantity):
        self.my_inventory[inventory_id] = {'product': product, 'quantity': quantity}
        # 加入表中
        sql = f'insert into {table2} values({inventory_id}, {product.product_id}, {quantity})'
        cursor.execute(sql)
        conn.commit()

    # 产品出库
    def remove_product(self, inventory_id, quantity):
        # 产品是否入库
        if inventory_id in self.my_inventory:
            # 数量是否足够
            current_quantity = self.my_inventory[inventory_id]['quantity']
            if current_quantity >= quantity:
                sql = f'update {table2} set quantity = {current_quantity}-{quantity} where inventory_id = {inventory_id}'
                cursor.execute(sql)
                conn.commit()

                self.my_inventory[inventory_id]['quantity'] -= quantity
                print('出库成功')
            else:
                print('库存不足，出库失败')
        else:
            print('该产品不在仓库')

p1 = Product('123', 'apple', 'AA', 12.3)
p1.add_product()
inventory = Inventory()
inventory.add_product(p1, '12345', 10)
inventory.remove_product('12345', 5)

# 关闭连接
cursor.close()
conn.close()