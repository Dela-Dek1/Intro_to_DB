import mysql.connector

def create_database(db_name):
    """Creates a MySQL database if it doesn't exist.

    Args:
        db_name (str): The name of the database to create.
    """
    try:
        # Connect to MySQL server (without specifying a database initially)
        mydb = mysql.connector.connect(
            host="localhost",  # Your MySQL host (usually localhost)
            user="your_mysql_user",  # Your MySQL username
            password="your_mysql_password"  # Your MySQL password
        )

        mycursor = mydb.cursor()

        # Check if the database exists (using a try-except block)
        try:
            mycursor.execute(f"CREATE DATABASE {db_name}")  # Attempt to create
            print(f"Database '{db_name}' created successfully!")
        except mysql.connector.errors.DatabaseError as err:
            if "1007" in str(err): # Error 1007 means database already exists
                print(f"Database '{db_name}' already exists.")
            else:
                print(f"An unexpected error occurred: {err}")  # Handle other errors
        finally:
          mydb.close() # Close the connection regardless of success or failure

    except mysql.connector.Error as err:
        print(f"Failed to connect to MySQL server: {err}")


if __name__ == "__main__":
    database_name = "alx_book_store"
    create_database(database_name)