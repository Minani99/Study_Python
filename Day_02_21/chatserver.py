# 서버와 클라이언트 통신
# 클라이언트 사이드


# GUI : tkinter / ttk / QT
# TCP & SOCKET : 통신 기반

# TCP transmisson control protocol로 통신 규칙
# TCP 특징 : 연결 지향적 -> TCP는 데이터를 보내기 전 서버와 클라이언트가 서로 확인 절차 (3way 핸드셰이크)가 있음.
# 3way핸드셰이크로 서로 확인 후 데이터에 대한 전송이 이루어짐
# 데이터 전송 신뢰성이 높다 : TCP는 데이터가 정확하게 전달되도록 보장해줌
# 예를들어 데이터가 전송 중 끊기거나 잘못 전달되면 다시 보내는 등 처리를 함

# 순서를 보장해줌(보내는 데이터가 엉키지 않도록)
# 보내고자하는 데이터가 12345 인 경우
# 여러 환경적 이유로 13245 등 데이터가 꼬이는 현상이 발생할 수 있는데, TCP는 이런 현상을 방지해줌

# 흐름제어
# (tick으로 양방향에서의 박자를 맞추는 것 처럼 서버와 클라이언트가 서로 데이터 송수신과정을 소화할 수 있는 흐름으로 제어)


# 3way handshake
# TCP 연결시 3웨이핸드셰이크 상세 과정
# 1.syn (송신자의 연결 요청)
# 2.syn-ack(수신자의 연결 요청 수락)
# 3.ack(송신자의 연결 확인)


# TCP의 연결 종료시 4way handshake과정으로 처리함
# 1.한쪽에서 연결종료 요청(FIN)
# 2.상대방은 1번 요청을 확인 (ACK)
# 3.상대방도 종료 준비가 되면 연결 종료 요청을 보냄(FIN)
# 4.송신자는 그 요청을 확인하고 연결을 완전히 종료 (ACK)


# 위 특징들로 TCP는 데이터가 정확하고 , 손실없이 송수신과정에서 신뢰성을 보장받으며 통신할 수 있도록 하는 규약

import socketserver # python에서 제공하는 TCP 서버 라이브러리, 클라이언트 요청을 처리하는 핸들러 클래스 설정을 위함
import threading # 여러 클라이언트 요청을 동시에 처리하기 위해 사용, 각크랄이언트 연결은 별도의 스레드에서 동작

HOST = '192.168.0.12'
PORT = 9900
lock = threading.Lock()  # 동기화 진행 스레드 / 다중 스레드 환경에서 데이터 경쟁 조건을 방지하기 위해 사용,
# 여러스레드가 동시에 users 데이터를 수정하지 못하도록 잠금 설정


class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send("등록된 사용자".encode())
            return None
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()
        self.sendMessageToAll('[%s]접속' % username)
        print('대화 참여 수 [%d]' % len(self.users))
        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s]접속해제' % username)
        print('대화 참여 수 [%d]' % len(self.users))

    def messageHandler(self, username, msg):
        if msg[0] != '/':
            self.sendMessageToAll("[%s] %s" % (username, msg))
            return
        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())


class myTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):
        print(self, 'self memory')
        print('client[%s]연결' % self.client_address[0])
        username = None
        try:
            username = self.registerUsername()
            print(username, ":username")
            msg = self.request.recv(1024)
            print(self.request)
            print(self.client_address)
            print(self.server)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)
        print("[%s]접속 종료" % self.client_address[0])
        self.userman.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.send('ID'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username


class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def runServer():
    try:
        server = ChatingServer((HOST, PORT), myTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("서버 종료")
        server.shutdown()
        server.server_close()


runServer()

# DATABASE : 프로젝트 데이터 관리
