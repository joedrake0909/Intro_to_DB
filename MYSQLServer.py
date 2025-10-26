#!/usr/bin/env python3
"""
MySQL Database Creation Script for ALX Book Store
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3306
        )
        
        if connection.is_connected():
            print("Connected to MySQL server successfully!")
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: Could not connect to MySQL server. {e}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()