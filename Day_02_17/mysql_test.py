import pymysql


def query(sql):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='0731',
        database='market_db',
        port=3306
    )
    cursor = connection.cursor()  # 커서란 SQL 쿼리를 실행하고 받아 오는 객체
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print('market_db내 table 정보')
    for table in tables:
        print(table[0])
    cursor.close()
    connection.close()
