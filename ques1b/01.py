def execute_insert_many(sql_query, input_list):
    cursor.executemany(sql_query, input_list)
    mydb.commit()
def insert_many_users(input_list):
    sql_query = "INSERT INTO users (email, password, username, phone, city, created_at) VALUES (%s, %s, %s, %s, %s, %s)" 
    execute_insert_many(sql_query, input_list)
def insert_many_retailers(input_list):
    sql_query = "INSERT INTO retailers(email, name , phone, password, street, city, province, pincode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_products(input_list):
    sql_query = "INSERT INTO products (name, category, retailer_id, price, created_at) VALUES (%s, %s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_novels(input_list):
    sql_query = "INSERT INTO novels (pdt_id, author, publisher, publication_date) VALUES (%s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_electronics(input_list):
    sql_query = "INSERT INTO electronics (pdt_id, category, brand, model) VALUES (%s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_addresses(input_list):
    sql_query = "INSERT INTO addresses (user_id, street, city, province, pincode) VALUES (%s, %s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_cart_items(input_list):
    sql_query = "INSERT INTO cart_items (user_id, pdt_id, quantity) VALUES (%s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_user_views(input_list):
    sql_query = "INSERT INTO user_views (pdt_id, user_id, created_at) VALUES (%s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_searches(input_list):
    sql_query = "INSERT INTO searches(user_id, body, created_at) VALUES (%s, %s, %s)"
    execute_insert_many(sql_query, input_list)
def insert_many_reviews(input_list):
    sql_query = "INSERT INTO reviews (pdt_id, user_id, username, rating) VALUES (%s, %s, %s, %s)"
    execute_insert_many(sql_query, input_list)

def insert_dummy_data():
    try:
        new_users = [('sachin@gmail.com', 'abcd', 'Sachin Yadav', 9972934723, 'Madrid', '2005-02-01 01:47:46'),
                  ('anuj@yahoo.com', 'abcd', 'Anuj Jain',
                   7502740385, 'Ludhiana', '2005-02-01 01:47:47'),
                  ('kavya@rediffmail.com', 'abcd', 'Kavya Agarwal',
                   2035753956, 'Madrid', '2005-02-01 01:47:48'),
                  ('niraj@gmail.com', 'abcd', 'Niraj Kumar',
                   7535765756, 'Delhi', '2005-02-01 01:47:49'),
                  ('anmol@yahoo.com', 'abcd', 'Anmol Gautam',
                   9383729512, 'Madrid', '2005-02-01 01:47:50'),
                  ('dhiraj@outlook.com', 'abcd', 'Dhiraj Sinha',
                   3829893782, 'Jaipur', '2005-02-01 01:47:51'),
                  ('kunal@iitgn.ac.in', 'abcd', 'Kunal Kumar',
                   6483026593, 'Delhi', '2005-02-01 01:47:52'),
                  ('aditya@iitgn.ac.in', 'abcd', 'Aditya Puri',
                   3289037502, 'Chandigarh', '2005-02-01 01:47:53'),
                  ('sushant.kumar@gmail.com', 'abcd', 'Sushant Kumar',
                   3792052942, 'Mumbai', '2005-02-01 01:47:54'),
                  ('kalyan.reddy@iitgn.ac.in', 'abcd', 'Kalyan G. Reddy',
                   3920395343, 'Mumbai', '2005-02-01 01:47:55'),
                  ('sushant.goyal@gmail.com', 'abcd', 'Sushant Goyal',
                   7583925935, 'Delhi', '2005-02-01 01:47:56'),
                  ('andy043@gmai.com', 'abcd', 'Andy Murray',
                   4832840284, 'Madrid', '2005-02-01 01:47:57'),
                  ('nicole58@yahoo.com', 'abcd', 'Nicole Ray',
                   8302643252, 'Madrid', '2005-02-01 01:47:58'),
                  ('jon380@rediffmail.com', 'abcd', 'Jon Duse',
                   7296937501, 'New York', '2005-02-01 01:47:59'),
                  ('ted.yeagar@gmail.com', 'abcd', 'Ted Yeagar',
                   9229247529, 'San Diego', '2005-02-01 01:48:00'),
                  ('eren.yeagar@gmail.com', 'abcd', 'Eren Yeagar',
                   4890850883, 'Shiganshina', '2005-02-01 01:48:01'),
                  ('mikasa.ackermann@gmail.com', 'abcd', 'Mikasa Ackermann',
                   7538925381, 'Shiganshina', '2005-02-01 01:48:02'),
                  ('armin.arlert@yahoo.com', 'abcd', 'Armin Arlert',
                   8539023535, 'Shiganshina', '2005-02-01 01:48:03'),
                  ('historia80@rediffmail.com', 'abcd', 'Historia Reiss',
                   8043253387, 'Ross', '2005-02-01 01:48:03'),
                  ('levi84@yahoo.com', 'abcd', 'Captain Levi', 3953647233, 'Maria', '2005-02-01 01:48:04')]
        insert_many_users(new_users)

        new_retailers = [('pvs840@gmail.com', 'PVS Ltd.', 3284002487, 'abcd', 'Linkoln Street', 'Ahmedabad', 'Gujarat', 840235),
                  ('cfd@gmail.com', 'CFD Ltd.', 7843963241, 'abcd',
                   'Gandhi Lane', 'Ahmedabad', 'Gujarat', 840785),
                  ('pravin@yahoo.com', 'Pravin Brothers and Co.',
                   9837295263, 'abcd', 'Plot 54', 'Delhi', 'Delhi', 392563),
                  ('nfs@rediffmail.com', 'NFS Pvt. Ltd.', 5792925363,
                   'abcd', 'Gramin Lane', 'Ludhiana', 'Punjab', 432985),
                  ('csd@gmail.com', 'CDS Pvt. Ltd.', 5403640253,
                   'abcd', 'Indranagar', 'Delhi', 'Delhi', 840263),
                  ('ydt@yahoo.com', 'YDT Bhandar', 4803284093, 'abcd',
                   'Linkoln Street', 'Ahmedabad', 'Gujarat', 840235),
                  ('bts@gmail.com', 'BTS Bazaar', 7382953636, 'abcd',
                   'Malviya Nagar', 'Ahmedabad', 'Gujarat', 830253),
                  ('netejs@yahoo.com', 'Neten Pvt. Ltd.', 8392846382, 'abcd',
                   'Nind Industrial Complex', 'Jaipur', 'Rajasthan', 328032),
                  ('lincoln@gmail.com', 'Lincoln Brothers', 9024626203,
                   'abcd', 'Dukar', 'Jaipur', 'Rajasthan', 325326),
                  ('pratap@gmail.com', 'Pratap Traders', 7892592623, 'abcd',
                   'Hinaya Building', 'Ahmedabad', 'Gujarat', 472932),
                  ('puona@rediffmail.com', 'Puona Traders', 7925292032,
                   'abcd', 'Vistras Center', 'Ahmedabad', 'Gujarat', 298532),
                  ('disco@gmail.com', 'Discoin Traders', 2908526202,
                   'abcd', 'Mistes', 'Jaipur', 'Rajasthan', 842223),
                  ('niagra@yahoo.com', 'Niagra Falls Pvt. Ltd', 8026830623,
                   'abcd', 'Vista', 'Bhopal', 'Madhya Pradesh', 274252),
                  ('nikon@rediffmail.com', 'Nikon Distributors', 8037342386,
                   'abcd', 'Nikon Building', 'Rewari', 'Haryana', 243563),
                  ('tekken@gmail.com', 'Tukaram Pvt. Ltd.', 7296332759,
                   'abcd', 'Tekken Cross', 'Ahmedabad', 'Gujarat', 840253),
                  ('fda@gmail.com', 'FDA Ltd.', 8403236732, 'abcd',
                   'FD building', 'Ahmedabad', 'Gujarat', 204252),
                  ('creates@yahoo.com', 'Creates Delhi Ltd.', 2035263343,
                   'abcd', 'Mahavir Marg', 'Delhi', 'Delhi', 203953),
                  ('tiny.ants@rediffmail.com', 'Tiny Ants Distributors', 3295328539,
                   'abcd', 'Akshardham Marg', 'Ahmedabad', 'Gujarat', 290842),
                  ('tuamir@gmail.com', 'Tuamir Co.', 3820529239, 'abcd',
                   'Buddha Road', 'Ahmedabad', 'Gujarat', 840235),
                  ('quench@rediffmail', 'Quench Pvt. Ltd.', 8303259322, 'abcd', 'Niagra Marg', 'Delhi', 'Delhi', 389253)]
        insert_many_retailers(new_retailers)

        # INSERT INTO products
        
        new_products = [('Da Vinci Code', 'novels', 2, 450, '2012-12-22 01:47:46'),
                  ('War and Peace', 'novels', 5, 1130, '2011-06-26 01:47:46'),
                  ('Ulysses', 'novels', 5, 530, '2019-05-31 01:47:46'),
                  ('The Lord of the Rings', 'novels',
                   2, 675, '2020-12-01 01:47:46'),
                  ('Inferno', 'novels', 2, 730, '2013-07-01 01:47:46'),
                  ('Lolita', 'novels', 3, 430, '2013-02-15 01:47:46'),
                  ('The Lost Symbol', 'novels', 3, 478, '2005-09-24 01:47:46'),
                  ('1984', 'novels', 6, 550, '2010-07-22 01:47:46'),
                  ('David Copperfield', 'novels', 3, 870, '2006-09-16 01:47:46'),
                  ('Angels and Demons', 'novels', 3, 699, '2013-10-01 01:47:46'),
                  ('Great Expectations', 'novels', 5, 120, '2007-10-13 01:47:46'),
                  ('Xiaomi S9 Pro', 'electronics',
                   1, 15000, '2015-02-09 01:47:46'),
                  ('Xiomi Note 4', 'electronics', 1, 20000, '2010-11-21 01:47:46'),
                  ('Neomi Watch R2', 'electronics',
                   8, 3600, '2008-02-10 01:47:46'),
                  ('LG Washing Machine M4', 'electronics',
                   7, 16500, '2015-12-01 01:47:46'),
                  ('Neomi Watch D5', 'electronics',
                   8, 11000, '2020-09-07 01:47:46'),
                  ('HP Paviliion G6', 'electronics',
                   7, 56000, '2016-01-06 01:47:46'),
                  ('Acer Predator Helio', 'electronics',
                   1, 74500, '2015-05-01 01:47:46'),
                  ('Dell Inspiron D3', 'electronics',
                   9, 45000, '2010-09-07 01:47:46'),
                  ('Dell Inspiron G4', 'electronics',
                   9, 55000, '2013-02-26 01:47:46'),
                  ('Apple macbook Air', 'electronics',
                   10, 85000, '2019-12-27 01:47:46'),
                  ('Realme R1 Pro', 'electronics',
                   1, 16000, '2011-11-29 01:47:46'),
                  ('Samsung Galaxy S9', 'electronics',
                   9, 20000, '2010-10-30 01:47:46'),
                  ('Leeves Men Jeans', 'clothes', 10, 1600, '2018-10-30 01:47:46'),
                  ('Apple macbook Pro', 'electronics',
                   9, 90000, '2020-12-30 01:47:46'),
                  ('Apple iPad Pro', 'electronics',
                   9, 60000, '2020-11-30 01:47:46'),
                  ('Apple iPad Air', 'electronics',
                   9, 54000, '2021-01-30 01:47:46'),
                  ('Apple iPad', 'electronics', 9, 35000, '2021-02-02 01:47:46')]
        insert_many_products(new_products)

        new_novels = [(1, 'Dan Brown', 'Penguin Books', '2016-08-05 01:47:46'),
                  (2, 'Leo Tolstoy', 'Pearson', '1956-04-01 01:47:46'),
                  (3, 'James Joyce', 'Penguin Books', '1992-12-20 01:47:46'),
                  (4, 'J.R.R. Tolkien', 'Pearson', '2011-11-21 01:47:46'),
                  (5, 'Dan Brown', 'Wiley', '2008-12-27 01:47:46'),
                  (6, 'Vladimir Nabokov', 'Penguin Books', '1960-02-22 01:47:46'),
                  (7, 'Dan Brown', 'Penguin Books', '2020-09-07 01:47:46'),
                  (8, 'George Orwell', 'Wiley', '1974-09-23 01:47:46'),
                  (9, 'Charles Dickens', 'Quarto', '2001-05-24 01:47:46'),
                  (10, 'Dan Brown', 'Quarto', '2015-01-01 01:47:46'),
                  (11, 'Charles Dickens', 'Pearson', '1932-12-03 01:47:46')]
        insert_many_novels(new_novels)

        new_electronics = [(12, 'Mobile', 'Xiaomi', 'S9'),
                  (13, 'Mobile', 'Xiaomi', 'Note 4'),
                  (14, 'Smartwatch', 'Neomi', 'R2'),
                  (15, 'Washing Machine', 'LG', 'M4'),
                  (16, 'Smartwatch', 'Neomi', 'D5'),
                  (17, 'Laptop', 'HP', 'G6'),
                  (18, 'Laptop', 'Acer', 'Helio93'),
                  (19, 'Laptop', 'Dell', 'D3'),
                  (20, 'Laptop', 'Dell', 'G4'),
                  (21, 'Laptop', 'Apple', 'air'),
                  (22, 'Mobile', 'Realme', 'R1'),
                  (23, 'Mobile', 'Samsung', 'S9'),
                  (25, 'Laptop', 'Apple', 'Pro'),
                  (26, 'Tablet', 'Apple', 'Pro'),
                  (27, 'Tablet', 'Apple', 'Air'),
                  (28, 'Tablet', 'Apple', '2018')]
        insert_many_electronics(new_electronics)

        sql_query = "INSERT INTO clothes (pdt_id, brand, model) VALUES (%s, %s, %s)"
        values = [(24, 'Leeves', 'SM slim M9')]
        cursor.executemany(sql_query, values)

        
        new_addresses = [(1, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013),
                  (2, 'Main Rd, Chick Pet', 'Bangalore', 'Karnataka', 560053),
                  (3, 'Shanti Park, Mira Road', 'Mumbai', 'Maharashtra', 401107),
                  (4, 'Paradise Cinema Lane, Mahim',
                   'Mumbai', 'Maharashtra', 40016),
                  (5, 'Shop 4, Mira Road', 'Mumbai', 'Maharashtra', 401107),
                  (6, 'Mahatama Chowk', 'Mumbai', 'Maharashtra', 400023),
                  (7, 'GT Karnal Rd', 'Delhi', 'Delhi', 110033),
                  (8, 'Vile Parle', 'Mumbai', 'Maharashtra', 400057),
                  (9,  'Shop 22, Hauz Khas', 'Delhi', 'Delhi', 110016),
                  (10, 'Office 1, Mit Corner', 'Pune', 'Maharashtra', 411011),
                  (11, '203, Maninagar', 'Ahmedabad', 'Gujarat', 380008),
                  (12, '39, Ans Patkar Road, Grant Road',
                   'Mumbai', 'Maharashtra', 400007),
                  (13, '6/85, W E A, Padam Singh Road, Karol Bagh',
                   'Delhi', 'Delhi', 110005),
                  (14, 'Rashi Bldg, 7 Poice Court Lane',
                   'Mumbai', 'Maharashtra', 400001),
                  (15, 'G15, 174/40, 8th F Main, 3rd Block, Jaynagar',
                   'Bangalore', 'Karnataka', 560011),
                  (16, '66, Mehdipatnam', 'Hyderabad', 'Andhra Pradesh', 500028),
                  (17, ' A/2, Vardhman Darshan, Jamli Galli, Borivali',
                   'Mumbai', 'Maharashtra', 400092),
                  (18, 'Near Post Office, Nehru Road, Santa Cruz (east)',
                   'Mumbai', 'Maharashtra', 400055),
                  (19, '58, 1719/2 Phase 3, Vatva',
                   'Ahmedabad', 'Gujarat', 382445),
                  (20, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)]
        insert_many_addresses(new_addresses)

        new_cart_items = [(1, 4, 3),
                  (1, 24, 1),
                  (19, 24, 6),
                  (3, 6, 1),
                  (1, 16, 1),
                  (4, 17, 1),
                  (2, 9, 1),
                  (4, 13, 1),
                  (5, 3, 20),
                  (6, 6, 1),
                  (7, 17, 1),
                  (7, 18, 1),
                  (8, 16, 10),
                  (9, 13, 1),
                  (10, 24, 2),
                  (11, 23, 1),
                  (2, 5, 2),
                  (12, 8, 1),
                  (13, 15, 1),
                  (14, 15, 1)]
        insert_many_cart_items(new_cart_items)

        # For User 1
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Vinci Code', '2010-01-06 01:47:46')")
        cursor.execute(
            "INSERT INTO user_views (pdt_id, user_id, created_at) VALUES (1, 1, '2010-01-06 02:44:00')")
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Inferno', '2010-01-06 04:47:46')")
        cursor.execute(
            "INSERT INTO user_views (pdt_id, user_id, created_at) VALUES (5, 1, '2010-01-07 02:44:00')")
        # Order 1
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (1, '2010-01-08 02:44:00', 730, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (1, 1, 5, 1, 730)")

        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Xiaomi', '2020-08-06 04:47:46')")
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Dell', '2020-09-20 04:47:46')")
        cursor.execute(
            "INSERT INTO user_views (pdt_id, user_id, created_at) VALUES (19, 1, '2020-10-10 02:44:00')")
        # Order 2
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (1, '2020-10-15 02:44:00', 45000, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (2, 1, 19, 1, 45000)")

        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Xiaomi', '2020-10-15 04:47:46')")
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Watch', '2020-10-20 04:47:46')")
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Lolita', '2020-11-01 04:47:46')")
        # Order 3
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (1, '2020-11-10 02:44:00', 480, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (3, 1, 6, 1, 450)")

        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'Apple', '2021-01-20 04:47:46')")
        cursor.execute(
            "INSERT INTO searches (user_id, body, created_at) VALUES (1, 'iPad', '2021-01-26 04:47:46')")

        new_user_views = [(6, 10, '2021-01-30 04:47:46'),
                  (6, 11, '2021-01-30 04:47:46'),
                  (6, 12, '2021-01-30 04:47:46'),
                  (6, 13, '2021-01-30 04:47:46'),
                  (6, 14, '2021-01-30 04:47:46'),
                  (6, 15, '2021-01-30 04:47:46'),
                  (6, 16, '2021-01-30 04:47:46'),
                  (6, 17, '2021-01-30 04:47:46'),
                  (6, 18, '2021-01-30 04:47:46'),
                  (6, 19, '2021-01-30 04:47:46'),
                  (6, 20, '2021-01-30 04:47:46'),

                  (14, 10, '2021-01-30 04:47:46'),
                  (14, 11, '2021-01-30 04:47:46'),
                  (14, 12, '2021-01-30 04:47:46'),
                  (14, 13, '2021-01-30 04:47:46'),
                  (14, 14, '2021-01-30 04:47:46'),
                  (14, 15, '2021-01-30 04:47:46'),
                  (14, 16, '2021-01-30 04:47:46'),
                  (14, 17, '2021-01-30 04:47:46'),
                  (14, 18, '2021-01-30 04:47:46'),
                  (14, 19, '2021-01-30 04:47:46'),
                  (14, 20, '2021-01-30 04:47:46'),

                  (24, 10, '2021-01-30 04:47:46'),
                  (24, 11, '2021-01-30 04:47:46'),
                  (24, 12, '2021-01-30 04:47:46'),
                  (24, 13, '2021-01-30 04:47:46'),
                  (24, 14, '2021-01-30 04:47:46'),
                  (24, 15, '2021-01-30 04:47:46'),
                  (24, 16, '2021-01-30 04:47:46'),
                  (24, 17, '2021-01-30 04:47:46'),
                  (24, 18, '2021-01-30 04:47:46'),
                  (24, 19, '2021-01-30 04:47:46'),
                  (24, 20, '2021-01-30 04:47:46'),

                  (24, 10, '2021-01-30 04:47:46'),
                  (24, 11, '2021-01-30 04:47:46'),
                  (24, 12, '2021-01-30 04:47:46'),
                  (24, 13, '2021-01-30 04:47:46'),
                  (24, 14, '2021-01-30 04:47:46'),
                  (24, 15, '2021-01-30 04:47:46'),
                  (24, 16, '2021-01-30 04:47:46'),
                  (24, 17, '2021-01-30 04:47:46'),
                  (24, 18, '2021-01-30 04:47:46'),
                  (24, 19, '2021-01-30 04:47:46'),
                  (24, 20, '2021-01-30 04:47:46'),

                  (5, 10, '2021-01-30 04:47:46'),
                  (5, 11, '2021-01-30 04:47:46'),
                  (5, 12, '2021-01-30 04:47:46'),
                  (5, 13, '2021-01-30 04:47:46'),
                  (5, 14, '2021-01-30 04:47:46'),
                  (5, 15, '2021-01-30 04:47:46'),
                  (5, 16, '2021-01-30 04:47:46'),
                  (5, 17, '2021-01-30 04:47:46'),
                  (5, 18, '2021-01-30 04:47:46'),
                  (5, 19, '2021-01-30 04:47:46'),
                  (5, 20, '2021-01-30 04:47:46'),

                  (9, 10, '2021-01-30 04:47:46'),
                  (9, 11, '2021-01-30 04:47:46'),
                  (9, 12, '2021-01-30 04:47:46'),
                  (9, 13, '2021-01-30 04:47:46'),
                  (9, 14, '2021-01-30 04:47:46'),
                  (9, 15, '2021-01-30 04:47:46'),
                  (9, 16, '2021-01-30 04:47:46'),
                  (9, 17, '2021-01-30 04:47:46'),
                  (9, 18, '2021-01-30 04:47:46'),
                  (9, 19, '2020-01-30 04:47:46'),
                  (9, 20, '2021-01-30 04:47:46'),

                  (7, 12, '2021-01-30 04:47:46'),
                  (7, 13, '2021-01-30 04:47:46'),
                  (7, 14, '2021-01-30 04:47:46'),
                  (7, 15, '2021-01-30 04:47:46'),
                  (7, 16, '2021-01-30 04:47:46'),
                  (7, 17, '2021-01-30 04:47:46'),
                  (7, 18, '2021-01-30 04:47:46'),
                  (7, 20, '2021-01-30 04:47:46')]
        insert_many_user_views(new_user_views)

        # Make some Orders and then reviews and ratings by user 4
        # Order 4
        cursor.execute("INSERT INTO orders(user_id, created_at, price, street, city, province, pincode) VALUES(4, '2020-11-06 02:44:00', 35000, 'Paradise Cinema Lane, Mahim', 'Mumbai', 'Maharashtra', 40016)")
        cursor.execute(
            "INSERT INTO order_items(order_id, user_id, pdt_id, quantity, price_of_each) VALUES(4, 4, 28, 1, 35000)")

        # Order 5
        cursor.execute("INSERT INTO orders(user_id, created_at, price, street, city, province, pincode) VALUES(4, '2020-11-10 02:44:00', 45000, 'Paradise Cinema Lane, Mahim', 'Mumbai', 'Maharashtra', 40016)")
        cursor.execute(
            "INSERT INTO order_items(order_id, user_id, pdt_id, quantity, price_of_each) VALUES(5, 4, 19, 1, 45000)")

        # Order 6
        cursor.execute("INSERT INTO orders(user_id, created_at, price, street, city, province, pincode) VALUES(4, '2020-11-13 02:44:00', 180, 'Paradise Cinema Lane, Mahim', 'Mumbai', 'Maharashtra', 40016)")
        cursor.execute(
            "INSERT INTO order_items(order_id, user_id, pdt_id, quantity, price_of_each) VALUES(6, 4, 11, 1, 120)")

        sql_query = "INSERT INTO reviews(pdt_id, user_id, username, rating, body, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [(28, 4, 'Niraj Kumar', 5, 'wonderful product, loved it!', '2020-12-09 03:36:45'),
                  (19, 4, 'Niraj Kumar', 3, 'NULL', '2020-12-11 03:36:45'),
                  (11, 4, 'Niraj Kumar', 4, 'Paper quality was okayish, otherwise wonderful reading', '2020-12-21 03:36:45')]
        cursor.executemany(sql_query, values)

        # Order 7
        cursor.execute("INSERT INTO orders(user_id, created_at, price, street, city, province, pincode) VALUES(2, '2018-11-13 02:44:00', 500, 'Main Rd, Chick Pet', 'Bangalore', 'Karnataka', 560053)")
        cursor.execute(
            "INSERT INTO order_items(order_id, user_id, pdt_id, quantity, price_of_each) VALUES(7, 2, 1, 1, 450)")
        # Order 8
        cursor.execute("INSERT INTO orders(user_id, created_at, price, street, city, province, pincode) VALUES(3, '2017-11-13 02:44:00', 1130, 'Shanti Park, Mira Road', 'Mumbai', 'Maharashtra', 401107)")
        cursor.execute(
            "INSERT INTO order_items(order_id, user_id, pdt_id, quantity, price_of_each) VALUES(8, 3, 2, 1, 1130)")

        sql_query = "INSERT INTO reviews (pdt_id, user_id, username, rating, body, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [(1, 2, 'Anuj Jain', 4, 'NULL', '2020-10-09 03:36:45'),
                  (2, 3, 'Kavya Agarwal', 3, 'I found the book to be okayish. The hype was not worth it.', '2020-09-11 03:36:45')]
        cursor.executemany(sql_query, values)

        # Order 9
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (3, '2018-11-13 02:44:00', 3250, 'Shanti Park, Mira Road', 'Mumbai', 'Maharashtra', 401107)")
        sql_query = "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (%s, %s, %s, %s, %s)"
        values = [(9, 3, 1, 6, 450),
                  (9, 3, 8, 1, 550)]
        cursor.executemany(sql_query, values)

        # Order 10
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (5, '2017-11-13 02:44:00', 20000, 'Shop 4, Mira Road', 'Mumbai', 'Maharashtra', 401107)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (10, 5, 13, 1, 20000)")

        # Order 11
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (12, '2016-11-13 02:44:00', 8000, '39, Ans Patkar Road, Grant Road', 'Mumbai', 'Maharashtra', 400007)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (11, 12, 24, 5, 1600)")

        # Orders for Last User

        # Order 12
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (20, '2016-11-13 02:44:00', 33000, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        cursor.execute(
            "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (12, 20, 16, 3, 33000)")

        # Order 13
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (20, '2017-11-13 02:44:00', 137600, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        sql_query = "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (%s, %s, %s, %s, %s)"
        values = [(13, 20, 24, 1, 1600),
                  (13, 20, 21, 1, 85000),
                  (13, 20, 28, 1, 35000),
                  (13, 20, 22, 1, 16000)]
        cursor.executemany(sql_query, values)

        # Order 14
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (20, '2018-11-13 02:44:00', 1205, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        sql_query = "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (%s, %s, %s, %s, %s)"
        values = [(14, 20, 3, 1, 530),
                  (14, 20, 4, 1, 675)]
        cursor.executemany(sql_query, values)

        # Order 15
        cursor.execute("INSERT INTO orders (user_id, created_at, price, street, city, province , pincode) VALUES (20, '2019-11-13 02:44:00', 1177, 'Gangamma Circle, Jalahalli', 'Bangalore', 'Karnataka', 560013)")
        sql_query = "INSERT INTO order_items (order_id, user_id, pdt_id, quantity, price_of_each) VALUES (%s, %s, %s, %s, %s)"
        values = [(15, 20, 10, 1, 699),
                  (15, 20, 7, 1, 478)]
        cursor.executemany(sql_query, values)

        # Cart of User 1 and User 2
        sql_query = "INSERT INTO cart_items(user_id, pdt_id, quantity) VALUES (%s, %s, %s)"
        values = [(1, 28, 2),
                  (1, 14, 1),
                  (1, 1, 5)]
        cursor.executemany(sql_query, values)

        sql_query = "INSERT INTO cart_items(user_id, pdt_id, quantity) VALUES (%s, %s, %s)"
        value = (2, 24, 2)
        cursor.execute(sql_query, value)

        new_searches = [(2, "mi", '2018-11-13 02:44:00'),
                  (3, "Jeans", '2018-11-15 02:44:00'),
                  (4, "watch", '2018-11-21 02:44:00'),
                  (5, "smart", '2018-10-13 02:44:00'),
                  (6, "Pro", '2018-12-13 02:44:00'),
                  (7, "Realme", '2019-11-13 02:44:00'),
                  (8, "Realme", '2020-11-13 02:44:00'),
                  (9, "Apple", '2019-11-13 02:44:00'),
                  (10, "iPad", '2006-11-13 02:44:00'),
                  (11, "mac", '2005-11-13 02:44:00'),
                  (12, "pple", '2010-11-13 02:44:00'),
                  (13, "sma", '2009-11-13 02:44:00'),
                  (14, "war and", '2008-11-13 02:44:00'),
                  (15, "Lolita", '2011-11-13 02:44:00'),
                  (16, "war", '2012-11-13 02:44:00'),
                  (18, "Demons", '2020-11-13 02:44:00'),
                  (20, "story", '2019-11-13 02:44:00'),
                  (5, "Xiaomi", '2017-11-13 02:44:00'),
                  (6, "Note", '2016-11-13 02:44:00'),
                  (7, "mac", '2015-11-13 02:44:00'),
                  (5, "iPad", '2014-11-13 02:44:00')]
        insert_many_searches(new_searches)

        new_reviews = [(21, 2, 'Anuj Jain', 4),
                  (19, 2, 'Anuj Jain', 1),
                  (18, 3, 'Kavya Agarwal', 2),
                  (17, 5, 'Anmol Gautam', 5),
                  (16, 2, 'Anuj Jain', 1),
                  (15, 2, 'Anuj Jain', 5),
                  (12, 2, 'Anuj Jain', 4),
                  (11, 2, 'Anuj Jain', 3),
                  (10, 5, 'Anmol Gautam', 4),
                  (6, 3, 'Anuj Jain', 4),
                  (5, 6, 'Dhiraj Sinha', 3),
                  (4, 7, 'Kunal Kumar', 4),
                  (3, 8, 'Aditya Puri', 5),
                  (2, 2, 'Anuj Jain', 1),
                  (1, 8, 'Aditya Puri', 4),
                  (9, 5, 'Anmol Gautam', 5),
                  (8, 2, 'Anuj Jain', 5),
                  (7, 8, 'Aditya Puri', 3),
                  (13, 2, 'Anuj Jain', 4),
                  (14, 5, 'Anmol Gautam', 2)]
        insert_many_reviews(new_reviews)
        mydb.commit()
    except Exception as e:
        print("Error while inserting dummy data reason", e)