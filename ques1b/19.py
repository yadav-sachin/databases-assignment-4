def find_retailer_for_user_id(user_id):
    cursor.execute("""
        SELECT DISTINCT retailer_id
        FROM products 
        WHERE pdt_id in (
            SELECT pdt_id 
            FROM order_items
            WHERE user_id = %s
        )""", (user_id, ))
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)

find_retailer_for_user_id(1)