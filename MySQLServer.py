import mysql.connector

# Replace 'your_username' and 'your_password' with your MySQL credentials
config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password'
}

connection = None
cursor = None

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Check for warnings to determine if the database was created
    if cursor.fetchwarnings():
        pass  # Database already exists
    else:
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    # Close cursor and connection
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()