def electronics_category_increasing_price(elec_category):
    cursor.execute("""
    SELECT pdt_id, electronic_id, name, electronics.category, electronics.brand, electronics.model, price
    FROM electronics JOIN products USING (pdt_id)
    WHERE electronics.pdt_id = products.pdt_id AND electronics.category = %s
    ORDER BY price ASC""", (elec_category, ))
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)

electronics_category_increasing_price('Laptop')