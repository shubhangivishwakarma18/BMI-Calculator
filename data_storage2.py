import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='internship',
            user='root',
            password='abcd1234'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def close_connection(connection):
    try:
        if connection.is_connected():
            connection.close()
    except Error as e:
        print(f"Error closing connection to MySQL database: {e}")


def store_bmi_data(username, weight, height, bmi):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO bmi (username, weight, height, bmi) VALUES (%s, %s, %s, %s)",
                       (username, weight, height, bmi))
        connection.commit()

        print("BMI data stored successfully")

    except Error as e:
        print(f"Error storing BMI data in MySQL: {e}")

    finally:
        cursor.close()
        close_connection(connection)


def retrieve_bmi_data(username):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM bmi WHERE username = %s", (username,))
        data = cursor.fetchall()

        return data

    except Error as e:
        print(f"Error retrieving BMI data from MySQL: {e}")
        return None

    finally:
        cursor.close()
        close_connection(connection)
