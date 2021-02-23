def fetch_top_n_movies_audience_rating(n, audience_rating, positive_sentiments):
    cursor.execute("""
        SELECT movie_id, movie_title, audience_rating, COUNT(*) AS 'positive_reviews_count'
        FROM movies NATURAL JOIN movie_reviews
        WHERE sentiment = 'positive'
        GROUP BY movie_id, movie_title, audience_rating
        HAVING COUNT(*) >= %s AND audience_rating > %s
        ORDER BY audience_rating DESC
        LIMIT %s
        """, (positive_sentiments, audience_rating, n) )
    output_list = cursor.fetchall()
    for row in output_list:
        print(*row)

fetch_top_n_movies_audience_rating(5, 3.50, 2)