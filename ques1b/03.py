def increment_price_below_recent_months(price_below, increase_percentage, viewed_user_count, recent_months): 
    cursor.execute("""
        UPDATE products
        SET price = price * %s
        where price < %s AND pdt_id IN (
            SELECT pdt_id 
            FROM user_views
            WHERE created_at >= DATE_SUB(CURDATE(),INTERVAL %s MONTH)
            GROUP BY pdt_id
            HAVING COUNT(DISTINCT user_id) > %s 
        )""", ( increase_percentage/100 + 1, price_below, recent_months, viewed_user_count))
    mydb.commit()

increment_price_below_recent_months(5000, 10, 10, 3)