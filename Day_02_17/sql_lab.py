import pymysql

DB_NAME = "minani_db"


def use_database(sql):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='0731',
        port=3306,
        database=DB_NAME
    )
    cursor = connection.cursor()
    cursor.execute(sql)

    tables = cursor.fetchall()
    for table in tables:
        print(table)

    connection.commit()
    cursor.close()
    connection.close()


use_database("DROP TABLE IF EXISTS BookInfo")
use_database("DROP TABLE IF EXISTS UserInfo")

use_database("""
CREATE TABLE UserInfo (
    name VARCHAR(50),
    age INT
)
""")
print("유저 테이블 생성 완료")

use_database("""
CREATE TABLE BookInfo (
    title VARCHAR(50),
    author VARCHAR(50)
)
""")
print("책 테이블 생성 완료")

use_database("""
INSERT INTO UserInfo(name, age) VALUES 
('박민환', 27),
('성진하', 29),
('김동현', 28);
""")
print("유저 데이터 삽입 완료")

use_database("""
INSERT INTO BookInfo(title, author) VALUES 
('너무', '눈이'),
('피곤한', '저절로'),
('하루', '감겨');
""")
print("책 데이터 삽입 완료")

use_database("""
SELECT UserInfo.name, UserInfo.age, BookInfo.title, BookInfo.author
FROM UserInfo
INNER JOIN BookInfo
""")
print("조인 완료")
