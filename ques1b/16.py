def users_with_cart_prdt_quantity(quantity_less_than):
    cursor.execute("""
        SELECT DISTINCT user_id, username, email, phone
        FROM users
        WHERE user_id in (
            SELECT user_id
            FROM cart_items
            WHERE quantity < %s
        )""", (quantity_less_than, ))
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)

users_with_cart_prdt_quantity(5)