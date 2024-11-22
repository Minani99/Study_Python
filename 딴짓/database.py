import mysql.connector
from mysql.connector import Error

db_config = {
    'host': '203.250.133.118',
    'user': 'host',
    'password': '0731',
    'database': 'auction_db'
}

#MySQL 데이터베이스 연결 함수

def connect_to_db():
    try:
        connections = mysql.connector.connect(**db_config)
        if connections.is_connected():
            print("Successfully connected to the database")
            return connections
    except Error as e:
        print(f"Error: {e}")
        return None

connection = connect_to_db()