def create_database_schema():
    cursor.execute("DROP DATABASE IF EXISTS RandomX")
    cursor.execute("CREATE DATABASE RandomX")
    cursor.execute("USE RandomX")
    
    cursor.execute("""
        CREATE TABLE users(
            username VARCHAR (50),
            gender ENUM("m", "f") NOT NULL,
            age INTEGER NOT NULL,
            PRIMARY KEY (username)
        )""")
    cursor.execute("""
        CREATE TABLE movies(
            movie_id VARCHAR (255),
            movie_title VARCHAR (255) NOT NULL,
            audience_rating FLOAT(4,2) NOT NULL,
            PRIMARY KEY (movie_id)
        )""")
    cursor.execute("""
        CREATE TABLE movie_reviews(
            movie_id VARCHAR (255) NOT NULL, 
            username VARCHAR (50) NOT NULL,
            movie_rev VARCHAR (500) NOT NULL,
            FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
            FOREIGN KEY (username) REFERENCES users(username)
        )""")
    mydb.commit()