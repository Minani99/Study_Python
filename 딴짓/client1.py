import socket
import threading
import tkinter as tk
from tkinter import simpledialog, ttk

HOST = '127.0.0.1'
PORT = 12345

class ChatClient:
    def __init__(root, root):
        root.root = root
        root.root.title("카카오톡 스타일 채팅 클라이언트")

        # 스크롤 가능한 프레임 생성
        root.main_frame = ttk.Frame(root)
        root.main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        root.canvas = tk.Canvas(root.main_frame, height=400)  # 고정된 높이 설정
        root.scrollbar = ttk.Scrollbar(root.main_frame, orient="vertical", command=root.canvas.yview)
        root.scrollable_frame = ttk.Frame(root.canvas)

        root.scrollable_frame.bind(
            "<Configure>",
            lambda e: root.canvas.configure(scrollregion=root.canvas.bbox("all"))
        )

        root.canvas.create_window((0, 0), window=root.scrollable_frame, anchor="nw")
        root.canvas.configure(yscrollcommand=root.scrollbar.set)

        root.canvas.grid(row=0, column=0, sticky="nsew")
        root.scrollbar.grid(row=0, column=1, sticky="ns")

        # 메시지 입력 영역
        root.message_entry = tk.Entry(root, width=40)
        root.message_entry.grid(row=1, column=0, padx=10, pady=10)
        root.message_entry.bind("<Return>", root.send_message)  # Enter 키로 메시지 전송

        # 전송 버튼
        root.send_button = tk.Button(root, text="전송", command=root.send_message)
        root.send_button.grid(row=1, column=1, padx=10, pady=10)

        # 소켓 연결
        root.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        root.client_socket.connect((HOST, PORT))

        # 닉네임 설정
        root.nickname = simpledialog.askstring("닉네임 입력", "사용할 닉네임을 입력하세요:", parent=root)
        if not root.nickname:
            root.nickname = "익명"  # 닉네임 미입력 시 기본값 설정
        root.client_socket.send(root.nickname.encode('utf-8'))  # 서버에 닉네임 전송

        # 수신 스레드 시작
        threading.Thread(target=root.receive_messages, daemon=True).start()

    def receive_messages(root):
        """서버로부터 메시지를 수신하여 채팅창에 표시"""
        while True:
            try:
                message = root.client_socket.recv(1024).decode('utf-8')
                print(f"Received message: {message}")  # 수신된 메시지 확인용 로그
                root.root.after(0, root.display_message, message, "left")  # 메인 스레드에서 UI 업데이트
            except Exception as e:
                print(f"Error receiving message: {e}")  # 예외 발생 시 로그
                break

    def send_message(root, event=None):
        """입력된 메시지를 서버로 전송하고 채팅창에 표시"""
        message = root.message_entry.get()
        if message:
            root.display_message(f"{root.nickname}: {message}", align="right")  # 송신 메시지는 오른쪽 정렬
            root.client_socket.send(message.encode('utf-8'))
            root.message_entry.delete(0, tk.END)  # 입력창 비우기

    def display_message(root, message, align="left"):
        """채팅창에 메시지 표시"""
        # 대화 구름 스타일 설정
        bubble_frame = ttk.Frame(root.scrollable_frame)
        bubble_frame.pack(fill="x", pady=5, padx=10, anchor="e" if align == "right" else "w")

        bubble_label = tk.Label(
            bubble_frame,
            text=message,
            wraplength=250,  # 최대 너비 설정
            bg="#DCF8C6" if align == "right" else "#FFFFFF",
            fg="#000000",
            font=("Arial", 10),
            padx=10,
            pady=5,
            bd=1,
            relief="solid",
            justify="left"
        )
        bubble_label.pack(anchor="e" if align == "right" else "w")  # 동일한 방식으로 정렬

        # 채팅창 자동 스크롤
        root.canvas.update_idletasks()
        root.canvas.yview_moveto(1.0)

    def on_close(root):
        """GUI 종료 시 소켓 닫기"""
        try:
            root.client_socket.close()
        except Exception as e:
            print(f"Error closing socket: {e}")
        root.root.destroy()

# 클라이언트 GUI 실행
if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", client.on_close)  # 창 닫기 이벤트 처리
    root.geometry("400x600")  # 클라이언트 창 크기 설정 (해상도 차이 문제 방지)
    root.mainloop()
