import mysql.connector
from mysql.connector import Error

# Connect to server
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
connection = create_connection("localhost", "root", "123456")

# access to database

# cursor = connection.cursor()
# cursor.execute('use northwind;')
# cursor.execute("select id, company from customers;")

# print data

# for info in cursor.fetchall():   
#     print(info[0], info[1])

connection.close()