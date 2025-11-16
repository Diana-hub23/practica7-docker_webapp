import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "rootpass"),
        database=os.getenv("MYSQL_DB", "testdb")
    )
