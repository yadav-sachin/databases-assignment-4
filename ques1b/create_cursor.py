import mysql.connector as mysql
import pandas as pd
try:

    mydb = mysql.connect(host='localhost', user='root',
                         password='mypass', auth_plugin='mysql_native_password')

except Exception as e:

    print(
        'Failed to create connection with mysql server, reason {0}'.format(e))

try:

    cursor = mydb.cursor(buffered=True)

except Exception as e:

    print('Error occur while creating cursor object, reason {0}'.format(e))
