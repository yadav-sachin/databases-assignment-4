def holi_discount_table(discount_percentage):
    cursor.execute("DROP TABLE IF EXISTS holi_Deals")
    mydb.commit()
    cursor.execute("""
        CREATE TABLE holi_Deals
        SELECT *
        FROM products
        WHERE created_at >= DATE_SUB(CURDATE(),INTERVAL 100 DAY)""")
    cursor.execute("""
        UPDATE holi_Deals
        SET price = price * %s""", (1 - discount_percentage/100, ))
    mydb.commit()

holi_discount_table(15)