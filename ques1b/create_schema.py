def create_database_schema():
    try:
        cursor.execute("DROP DATABASE IF EXISTS x")
        cursor.execute("CREATE DATABASE x")
        cursor.execute("USE x")

        cursor.execute("""
            CREATE TABLE users(
                user_id INT NOT NULL AUTO_INCREMENT,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(100) NOT NULL,
                username VARCHAR(100) NOT NULL,
                phone NUMERIC(10,0) NOT NULL UNIQUE,
                city VARCHAR(100),
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id)
        )""")

        cursor.execute("""
        CREATE TABLE retailers(
            retailer_id INT NOT NULL AUTO_INCREMENT,
            email VARCHAR(100) NOT NULL UNIQUE,
            name VARCHAR(100) NOT NULL,
            phone NUMERIC(10,0) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            street VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            province VARCHAR(100) NOT NULL,
            pincode NUMERIC(6, 0) NOT NULL,
            PRIMARY KEY (retailer_id)
        )""")

        cursor.execute("""
        CREATE TABLE products(
            pdt_id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            category ENUM('novels', 'electronics', 'clothes') NOT NULL,
            retailer_id INT NOT NULL,
            price NUMERIC(10,2) NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (pdt_id),
            FOREIGN KEY (retailer_id) REFERENCES retailers(retailer_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE user_views(
            view_id INT NOT NULL AUTO_INCREMENT,
            pdt_id INT NOT NULL,
            user_id INT NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (view_id),
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE searches(
            search_id INT NOT NULL AUTO_INCREMENT,
            user_id INT NOT NULL,
            body VARCHAR (100) NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (search_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE addresses(
            address_id INT NOT NULL AUTO_INCREMENT,
            user_id INT NOT NULL,
            street VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            province VARCHAR(100) NOT NULL,
            pincode NUMERIC(6, 0) NOT NULL,
            PRIMARY KEY (address_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE novels(
            novel_id INT NOT NULL AUTO_INCREMENT,
            pdt_id INT NOT NULL,
            author VARCHAR(100) NOT NULL,
            publisher VARCHAR(100),
            publication_date DATE NOT NULL ,
            description VARCHAR(1000),
            PRIMARY KEY (novel_id),
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE electronics(
            electronic_id INT NOT NULL AUTO_INCREMENT,
            pdt_id INT NOT NULL,
            category VARCHAR(100) NOT NULL,
            brand VARCHAR(100) NOT NULL,
            model VARCHAR(100) NOT NULL,
            description VARCHAR(1000),
            date_of_manufacture DATE,
            PRIMARY KEY (electronic_id),
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE clothes(
            cloth_id INT NOT NULL AUTO_INCREMENT,
            pdt_id INT NOT NULL,
            brand VARCHAR(100) NOT NULL,
            model VARCHAR(100),
            description VARCHAR(1000),
            PRIMARY KEY (cloth_id),
            FOREIGN KEY (pdt_id) REFERENCES products (pdt_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE reviews(
            review_id INT NOT NULL AUTO_INCREMENT,
            pdt_id INT NOT NULL,
            user_id INT,
            username VARCHAR(100) NOT NULL,
            rating NUMERIC(2,0) NOT NULL,
            body VARCHAR (1000),
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (review_id),
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )""")

        cursor.execute("""CREATE TABLE cart_items(
            cart_item_id INT NOT NULL AUTO_INCREMENT,
            user_id INT NOT NULL,
            pdt_id INT NOT NULL,
            quantity INT NOT NULL DEFAULT 1,
            PRIMARY KEY (cart_item_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE orders(
            order_id INT NOT NULL AUTO_INCREMENT,
            user_id INT NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            price NUMERIC(10,2) NOT NULL,
            street VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            province VARCHAR(100) NOT NULL,
            pincode NUMERIC(6, 0) NOT NULL,
            PRIMARY KEY (order_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )""")

        cursor.execute("""
        CREATE TABLE order_items(
            order_item_id INT NOT NULL AUTO_INCREMENT,
            order_id INT NOT NULL,
            user_id INT NOT NULL,
            pdt_id INT NOT NULL,
            quantity INT NOT NULL DEFAULT 1,
            price_of_each NUMERIC(10,2) NOT NULL,
            PRIMARY KEY (order_item_id),
            FOREIGN KEY (pdt_id) REFERENCES products(pdt_id) ON DELETE CASCADE,
            FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )""")
        mydb.commit()
    except Exception as e:
        print('Error occur while creating schema, reason {0}'.format(e))