def delete_user(email):
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
        user_list = cursor.fetchall()
        if not user_list:
            raise Exception("No user found with the given email")
        cursor.execute("""
            UPDATE reviews
            SET user_id = NULL, username = 'Anonymous'
            WHERE user_id = (SELECT user_id
            FROM users
            WHERE email = %s)""",
                       (email, ))

        cursor.execute("""
            DELETE FROM users
            WHERE email = %s""",
                       (email, ))
        mydb.commit()
    except Exception as err:
        print("Error while deleting user: ", err)

delete_user('niraj@gmail.com')