def top_recommendations_user_id(user_id):
    cursor.execute("""
        SELECT pdt_id, name, price
        FROM (
            SELECT user_id, searches.created_at, pdt_id
            FROM searches, products
            WHERE name LIKE CONCAT('%%', body, '%%')
        ) T INNER JOIN products USING(pdt_id)
        WHERE T.user_id = %s AND pdt_id NOT IN (
            SELECT pdt_id
            FROM order_items
            WHERE user_id = %s
        )
        GROUP BY pdt_id
        ORDER BY MAX(T.created_at) DESC
        LIMIT 10""", (user_id, user_id))
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)
        
top_recommendations_user_id(1)