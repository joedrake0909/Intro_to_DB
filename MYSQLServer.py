import mysql.connector
import os

try:
    # Get database credentials from environment variables
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASS", "")
    port = os.getenv("DB_PORT", "3306")

    # Connect to MySQL server (no database yet)
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )

    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
