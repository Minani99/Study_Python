# GUI + DB MTSQL 연습문제
# GUI 프로그램을 통해 MYSQL 서버의 데이터베이스 생성 및 수정 관리를 할 수 있도록 구현
# GUI를 통한 DB의 CRUD 작업
# 1 DB생성, 테이블 생성 데이터 USE설정
# 2 특정 테이블의 데이터 삽임
# 3 특정 테이블의 데이터 검색 결과 조회 (데이터가 SQL 문법에 적합한지 검사하는 함수)
# 4 특정 테이블의 데이터 검색 결과 조회 (select 기능인데 전체열 or 특정열)
# 5 테이블 삭제 (어떤 테이블 삭제할건지 지정)

import pymysql
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = ""  # 현재 사용 중인 데이터베이스


def use_database(sql):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306,
            database=DB_NAME if DB_NAME else None  # DB_NAME이 없을 경우 None
        )
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("DB 오류", str(e))