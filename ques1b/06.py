def find_products_like_and_users_bought(like_string):
    cursor.execute("""
        SELECT name, pdt_id, user_id
            FROM (
                SELECT name, pdt_id
                FROM products 
                WHERE name LIKE %s
            )P LEFT OUTER JOIN (
                SELECT DISTINCT user_id, pdt_id
                FROM order_items
            )O USING (pdt_id)""", ('%' + like_string + '%', ))
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)

find_products_like_and_users_bought('mi')