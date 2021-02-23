def find_users_reside_city_purchase_greater(city_name, purchase_greater_equal):
    cursor.execute("""
        SELECT DISTINCT phone, email 
        FROM users
        where city = %s AND user_id IN (
            SELECT user_id 
            FROM orders
            GROUP BY user_id
            HAVING SUM(price) >= %s
        )""", (city_name, purchase_greater_equal));
    user_list = cursor.fetchall()

    for info in user_list:
        print(*info)

find_users_reside_city_purchase_greater('Madrid', 1000)