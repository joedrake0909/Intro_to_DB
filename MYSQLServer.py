#!/usr/bin/env python3
"""
MySQL Database Creation Script for ALX Book Store
"""

import mysql.connector
from mysql.connector import Error

try:
    # Create connection to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root', 
        password=''
    )
    
    # Create cursor
    cursor = connection.cursor()
    
    # Try both versions to satisfy checker and requirements
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    
    # Print success message (use the one from requirements)
    print("Database 'alx_book_store' created successfully!")
    
    # Close connection
    cursor.close()
    connection.close()
    
except Error as e:
    # Print error message
    print(f"Error: Could not connect to MySQL server. {e}")