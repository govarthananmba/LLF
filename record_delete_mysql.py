import mysql.connector
from mysql.connector import Error

def delete_all_data():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='djangoawsdb.cj6cqycks289.ap-southeast-2.rds.amazonaws.com',
            user='admin',
            password='Govar768LLF',
            database='djangodb'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Replace 'your_table_name' with the name of your table
            delete_query = "DELETE FROM app_record"
            cursor.execute(delete_query)
            connection.commit()  # Make sure to commit the changes
            print("All data has been deleted successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    delete_all_data()
