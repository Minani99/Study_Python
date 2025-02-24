# DB
# 1.귓속말 주고받기
## 보내는 표기 >>>  / 받는 표기 <<<   / 둘에게만 보이게 처리  / 색상을 전체대화 색상과 다르게
# 2. 받은 귓속말 텍스트를 마우스로 누르면 보내온 사람에게 답장모드로 변환
## /w 아이디 보내려는텍스트
# 3.강제퇴장 기능 - 관리자 권한
# 4.채팅금지/해제 기능 - 관리자 권한
# 5.관리자 계정 기능 - DB에 회원 계정 테이블이 존재한다.
# 6.DB에회원계정 테이블에 존재하는 회원만 로그인 ID/PW방식으로 로그인하여 대화방에 진입한다.

# 2.DB연동하기
# 각자 로컬 MYSQL서버를 이용해서 현재 대화방의 로그를 기록한다.
# 접속자의 오늘 로그인 여부
# 접속자로그의 테이블은 1일 1개 생성
# 대화방로그의 테이블은 모든 텍스트 기록이 담긴다.
# 강제퇴장인원/채팅금지관련로그
# ===>스레드로 하나 만들어서 관리?


import socketserver  # python에서 제공하는 TCP 서버 라이브러리, 클라이언트 요청을 처리하는 핸들러 클래스 설정을 위함
import threading  # 여러 클라이언트 요청을 동시에 처리하기 위해 사용, 각클라이언트 연결은 별도의 스레드에서 동작
import pymysql
from datetime import datetime

HOST = '192.168.0.12'
PORT = 9900
lock = threading.Lock()  # 동기화 진행 스레드 / 다중 스레드 환경에서 데이터 경쟁 조건을 방지하기 위해 사용,


# DATABASE : 프로젝트 데이터 관리
# params: SQL 쿼리의 %s 자리에 동적으로 값 전달
# fetch: 조회 쿼리에서 결과값을 반환할지 여부
def use_database(sql, params=None, fetch=False):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306,
            database='chat_db'
        )
        cursor = connection.cursor()
        cursor.execute(sql, params)

        result = None
        if fetch:
            result = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return result
    except pymysql.MySQLError as e:
        print("DB 오류:", str(e))
        return None


def log_message(username, message):
    date_table = datetime.now().strftime("chat_logs_%Y%m%d")
    # 테이블이 존재하지 않으면 생성
    sql_create = f"""
    CREATE TABLE IF NOT EXISTS {date_table} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50),
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    use_database(sql_create)

    # 메시지 기록
    sql_insert = f"INSERT INTO {date_table} (username, message) VALUES (%s, %s)"
    use_database(sql_insert, (username, message))


def log_private_message(sender, receiver, message):
    sql = "INSERT INTO private_logs (sender, receiver, message) VALUES (%s, %s, %s)"
    use_database(sql, (sender, receiver, message))


def authenticate_user(username, password):
    sql = "SELECT password, is_admin FROM users WHERE username=%s"
    result = use_database(sql, (username,), fetch=True)

    if result:
        stored_password, is_admin = result[0]
        return stored_password == password, bool(is_admin)  # T, T >> 관리자 / T, F >> 유저
    return False, False  # 로그인 실패


class UserManager:
    def __init__(self):
        self.banned_users = []
        self.users = {}

    def add_user(self, username, conn, addr):  # 유저 추가
        if username in self.users:
            conn.send("등록된 사용자".encode())
            return None
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()
        self.send_message_to_all('[%s]접속' % username)
        print('대화 참여 수 [%d]' % len(self.users))
        return username

    def remove_user(self, username):  # 유저 삭제
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.send_message_to_all('[%s]접속해제' % username)
        print('대화 참여 수 [%d]' % len(self.users))

    def message_handler(self, username, msg):
        if username in self.banned_users:
            sender_conn, _ = self.users[username]
            sender_conn.send(">>> [시스템] 님 채금임.".encode())
            return

        if msg[0] != '/':  # '/'가 안들어 있다면
            self.send_message_to_all("[%s] %s" % (username, msg))  # 그냥 채팅
            log_message(username, msg)
            return

        private_command = msg.strip().split(' ', 2)  # 메시지를 공백으로 잘라 보관 (2번 자른다는 뜻 => 3개)
        if private_command[0] == '/w':  # 잘랐을때 앞에가 '/w'로 시작한다면
            self.send_message_to_private(username, private_command)  # 귓말을 보낼꺼임
            log_private_message(username, private_command[1], private_command)
        elif private_command[0] == '/kick':  # 킥
            self.kick_user(username, private_command[1])
        elif private_command[0] == '/ban':
            self.ban_user(username, private_command[1])
        elif private_command[0] == '/unban':
            self.unban_user(username, private_command[1])
        elif msg.strip() == '/quit':
            self.remove_user(username)
            return -1

    def kick_user(self, user_name, target_username):
        if user_name == 'admin':
            if target_username in self.users:
                target_conn, _ = self.users[target_username]
                target_conn.send(">>> [시스템] 강제 퇴장당했습니다.".encode())
                print("강퇴 완료")
                self.remove_user(target_username)
                target_conn.close()
                return
            else:
                print(f"{target_username} 사용자가 없습니다")
                return
        else:
            print("[시스템] 관리자 권한이 없습니다.")
            return

    def ban_user(self, user_name, target_username):
        if user_name == 'admin':
            target_conn, _ = self.users[target_username]
            target_conn.send(">>> [시스템] 당신 채금.".encode())
            self.banned_users.append(target_username)
            print("벤 목록 추가 완료")
            print(f"{target_username} 채팅 금지")
            return
        else:
            print("[시스템] 관리자 권한이 없습니다.")
            return

    def unban_user(self, user_name, target_username):
        if user_name == 'admin':
            if target_username in self.banned_users:
                target_conn, _ = self.users[target_username]
                target_conn.send(">>> [시스템] 채금 풀림.".encode())
                self.banned_users.remove(target_username)
                print("벤 목록에서 지우기 완료")
                return f">>> [시스템] {target_username}님의 채팅 금지를 해제했습니다."
            else:
                return f">>> [시스템] {target_username}님은 채팅 금지 상태가 아닙니다."

        else:
            return ">>> [시스템] 관리자 권한이 없습니다."

    def send_message_to_all(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())

    def send_message_to_private(self, username, private_command):
        if len(private_command) < 3:
            sender_conn, _ = self.users[username]
            sender_conn.send(">>> 귓속말 형식: /w [대상유저] [메시지]".encode())
            return

        target_user = private_command[1]
        private_msg = private_command[2]

        if target_user in self.users:
            target_conn, _ = self.users[target_user]
            sender_conn, _ = self.users[username]

            # 수신자 귓속말 전송
            target_conn.send(f"<<< [귓속말 from {username}] {private_msg}".encode())

            # 송신자 메시지 전송
            sender_conn.send(f">>> [귓속말 to {target_user}] {private_msg}".encode())
        else:
            sender_conn, _ = self.users[username]
            sender_conn.send(f">>> [시스템] {target_user} 사용자가 존재하지 않습니다.".encode())


# ---------------------------------------------------------------------------------------------

class MyTcpHandler(socketserver.BaseRequestHandler):  # 상속 받아옴
    user_mange = UserManager()  # 사용자 관리 객체 ( 접속한 유저)

    def handle(self):  # 클라이언트 연결 처리
        print(f"client[{self.client_address[0]}] 연결")
        username = None
        is_admin = False
        try:
            while True:
                msg = self.request.recv(1024).decode()
                if not msg:
                    break  # 연결 종료 시 루프 탈출

                if msg.startswith("LOGIN"):
                    _, username, password = msg.split(' ', 2)
                    success, is_admin = authenticate_user(username, password)  # 튜플로 나온 부울값

                    if success:
                        self.username = username
                        self.is_admin = is_admin
                        self.request.send("LOGIN_SUCCESS".encode())
                        self.user_mange.add_user(username, self.request, self.client_address)
                        print(f"{username} 로그인 성공 (관리자: {is_admin})")
                    else:
                        self.request.send("LOGIN_FAILED".encode())
                        self.request.close()

                elif hasattr(self, 'username'):
                    if self.user_mange.message_handler(username, msg) == -1:
                        self.request.close()
                        break
                else:
                    self.request.send("로그인 먼저.".encode())

        except Exception as e:
            print(f"무언가 에러 발생: {e}")

        finally:
            if hasattr(self, 'username'):
                self.user_mange.remove_user(self.username)
            print(f"[{self.client_address[0]}] 접속 종료")

    def register_username(self):
        while True:
            self.request.send('ID'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.user_mange.add_user(username, self.request, self.client_address):
                return username


# --------------------------------------------------------------------------------------------


class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def run_server():
    server = None
    try:
        server = ChatServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("서버 종료")
        server.shutdown()
        server.server_close()


run_server()
