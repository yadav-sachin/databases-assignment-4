def insert_user(username, gender, age):
    sql_query = "INSERT INTO users VALUES (%s, %s, %s)"
    values = (username, gender, age)
    cursor.execute(sql_query, values)
    mydb.commit()

def insert_movie(movie_id, movie_title, audience_rating):
    sql_query = "INSERT INTO movies VALUES (%s, %s, %s)"
    values = (movie_id, movie_title, audience_rating)
    cursor.execute(sql_query, values)
    mydb.commit()
    
def insert_movie_review(movie_id, username, movie_rev):
    sql_query = "INSERT IGNORE INTO movie_reviews VALUES (%s, %s, %s)"
    values = (movie_id, username, movie_rev)
    cursor.execute(sql_query, values)
    mydb.commit()

user_df = pd.read_excel('userdata.xls')

for index, row in user_df.iterrows():
    insert_user(row['username'], row['gender'], row['age'])

cursor.execute("SELECT * FROM users")
output_list = cursor.fetchall()
for row in output_list:
    print(*row)

movie_df = pd.read_excel(
     "movie_info.xlsx",
     engine='openpyxl'
)

for index, row in movie_df.iterrows():
    insert_movie(row['movie_id'], row['movie_title'], row['audience_rating'])

movie_review_df = pd.read_excel('movie_reviews.xls')

for index, row in movie_review_df.iterrows():
    insert_movie_review(row['movie_id'], row['user_name'], row['movie_rev'])