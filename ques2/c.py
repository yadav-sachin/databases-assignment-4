positive_text_file = open('positive_words.txt', 'r')
positive_list = positive_text_file.read().splitlines()

negative_text_file = open('negative_words.txt', 'r')
negative_list = negative_text_file.read().splitlines()

def alter_table_add_column_sentiment():
    cursor.execute("""ALTER TABLE movie_reviews
                    ADD sentiment ENUM('positive', 'negative', 'neutral') NOT NULL DEFAULT 'neutral'
                    """)
    mydb.commit()

alter_table_add_column_sentiment()

def get_movie_sentiment(movie_rev):
    sentiment_score = 0
    words = movie_rev.split()
    for word in words:
        if word in positive_list:
            sentiment_score += 1
        elif word in negative_list:
            sentiment_score -= 1
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    return 'neutral'

def update_movie_setiment(movie_id, username, movie_rev):
    movie_sentiment = get_movie_sentiment(movie_rev)
    sql_query = """
        UPDATE movie_reviews
        SET sentiment = %s
        WHERE movie_id = %s AND username = %s AND movie_rev = %s
        """
    values = (movie_sentiment, movie_id, username, movie_rev)
    cursor.execute(sql_query, values)
    mydb.commit()

cursor.execute("SELECT * FROM movie_reviews")
output_list = cursor.fetchall()
for row in output_list:
    movie_id, username, movie_rev = row[:3]
    update_movie_setiment(movie_id, username, movie_rev)