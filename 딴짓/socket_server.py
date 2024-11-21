import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = {}  # 클라이언트 소켓과 닉네임 매핑


def broadcast(message, sender_socket):
    """모든 클라이언트에게 메시지를 브로드캐스트"""
    for client_socket in clients.keys():
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                client_socket.close()
                del clients[client_socket]


def handle_client(client_socket):
    """클라이언트의 메시지 수신 및 처리"""
    try:
        # 닉네임 수신
        nickname = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = nickname
        print(f"닉네임 {nickname} 연결됨.")

        # 다른 클라이언트에게 알림
        broadcast(f"{nickname}님이 채팅에 참여했습니다!".encode('utf-8'), client_socket)

        while True:
            message = client_socket.recv(1024)  # 메시지 수신
            if not message:
                break
            broadcast(f"{nickname}: {message.decode('utf-8')}".encode('utf-8'), client_socket)
    except:
        pass
    finally:
        # 클라이언트 종료 처리
        nickname = clients.get(client_socket, "알 수 없음")
        print(f"{nickname} 연결 종료.")
        broadcast(f"{nickname}님이 채팅을 떠났습니다.".encode('utf-8'), client_socket)
        client_socket.close()
        del clients[client_socket]


def start_server():
    """서버 시작"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"서버 실행 중 {HOST}:{PORT}")

    while True:
        client_socket, _ = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    start_server()
