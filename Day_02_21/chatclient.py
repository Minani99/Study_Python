import socket
from threading import Thread
import tkinter
from tkinter import ttk, messagebox

# === 기본 GUI 설정 === #
tk = tkinter.Tk()
tk.title("민카오톡")
tk.geometry("400x600")
tk.configure(bg='#F5F5F5')

# === 글로벌 변수 === #
sock = None
user_id = None

# === 로그인 프레임 === #
login_frame = tkinter.Frame(tk, bg='#F5F5F5')
login_frame.pack(fill=tkinter.BOTH, expand=True)

login_label = tkinter.Label(login_frame, text="로그인", font=('맑은 고딕', 18, 'bold'), bg='#F5F5F5')
login_label.pack(pady=20)

id_label = tkinter.Label(login_frame, text="아이디", font=('맑은 고딕', 12), bg='#F5F5F5')
id_label.pack(pady=5)
id_entry = ttk.Entry(login_frame)
id_entry.pack(pady=5)

password_label = tkinter.Label(login_frame, text="비밀번호", font=('맑은 고딕', 12), bg='#F5F5F5')
password_label.pack(pady=5)
password_entry = ttk.Entry(login_frame, show='*')
password_entry.pack(pady=5)

login_button = tkinter.Button(
    login_frame,
    text="로그인",
    font=('맑은 고딕', 12),
    bg='#D3D3D3',
    relief=tkinter.FLAT,
    command=lambda: login()
)
login_button.pack(pady=20)

# === 채팅 프레임 === #
chat_frame = tkinter.Frame(tk, bg='white', bd=2, relief=tkinter.GROOVE)

scrollbar = tkinter.Scrollbar(chat_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

entry2 = tkinter.Listbox(
    chat_frame,
    height=20,
    width=50,
    font=('맑은 고딕', 12),
    yscrollcommand=scrollbar.set,
    bd=0,
    highlightthickness=0,
    relief=tkinter.FLAT
)
entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
scrollbar.config(command=entry2.yview)

# === 입력 프레임 === #
input_frame = tkinter.Frame(tk, bg='#D3D3D3')

entry = tkinter.Entry(input_frame, font=('맑은 고딕', 12), width=30, relief=tkinter.GROOVE, bd=2)
entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=5, pady=5)

send_button = tkinter.Button(
    input_frame,
    text='전송',
    font=('맑은 고딕', 12, 'bold'),
    bg='#D3D3D3',
    relief=tkinter.FLAT,
    activebackground='#FFEB3B',
    command=lambda: onClick(sock)
)
send_button.pack(side=tkinter.RIGHT, padx=5)

# === 서버 정보 === #
HOST = '192.168.0.12'
PORT = 9900


# === 로그인 함수 === #
def login():
    global user_id, sock

    username = id_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("입력 오류", "아이디와 비밀번호를 모두 입력하세요.")
        return

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        # 서버에 로그인 정보 전송
        login_info = f"LOGIN {username} {password}"
        sock.send(login_info.encode())

        # 서버 응답 대기
        response = sock.recv(1024).decode()
        if response == "LOGIN_SUCCESS":
            user_id = username
            messagebox.showinfo("로그인 성공", f"{username}님, 환영합니다!")
            show_chat_window()  # 채팅 화면으로 전환
            Thread(target=rcvMsg, args=(sock,), daemon=True).start()
        else:
            messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 올바르지 않습니다.")
            sock.close()

    except Exception as e:
        messagebox.showerror("연결 오류", f"서버에 연결할 수 없습니다: {e}")


# === 채팅 화면 표시 === #
def show_chat_window():
    login_frame.pack_forget()  # 로그인 화면 숨기기
    chat_frame.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
    input_frame.pack(fill=tkinter.X, side=tkinter.BOTTOM, padx=10, pady=10)
    entry.bind("<Return>", onEnter)  # 엔터키로 메시지 전송
    entry2.bind("<Button-1>", on_message_click)  # 메시지 클릭 이벤트 바인딩


# === 메시지를 수신하는 함수 === #
def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            msg = data.decode()

            # 받은 메시지에 따라 색상 설정
            if "<<< [귓속말 from" in msg:
                entry2.insert(tkinter.END, msg)
                entry2.itemconfig(tkinter.END, {'fg': 'green'})  # 받은 귓속말 (초록색)
            elif ">>> [귓속말 to" in msg:
                entry2.insert(tkinter.END, msg)
                entry2.itemconfig(tkinter.END, {'fg': 'blue'})  # 보낸 귓속말 (파란색)
            elif "[admin]" in msg:
                entry2.insert(tkinter.END,   msg)
                entry2.itemconfig(tkinter.END, {'fg': 'red'})  # 어드민 색
            else:
                entry2.insert(tkinter.END,   msg)

            entry2.update()
            entry2.see(tkinter.END)
        except:
            break


# === 메시지를 전송하는 함수 === #
def onClick(sock):
    msg = entry.get().strip()
    if msg:
        if msg.startswith('/w '):
            values = msg.split(' ', 2)
            if len(values) < 3:
                entry2.insert(tkinter.END, '>>> 귓속말 형식: /w [대상유저] [메시지]')
                entry2.itemconfig(tkinter.END, {'fg': 'red'})
                return
            target_user = values[1]
            private_msg = values[2]
            sock.send(f"/w {target_user} {private_msg}".encode())
        else:
            sock.send(msg.encode())
        entry.delete(0, tkinter.END)


# === 엔터키로 전송 기능 === #
def onEnter(event):
    onClick(sock)


# === 귓속말 메시지를 클릭하면 자동으로 명령어 입력 === #
def on_message_click(event):
    selected_index = entry2.curselection()
    if selected_index:
        msg = entry2.get(selected_index[0])
        if "<<< [귓속말 from" in msg:
            start = msg.find("from") + 5
            end = msg.find("]", start)
            sender_username = msg[start:end].strip()
            entry.delete(0, tkinter.END)
            entry.insert(0, f"/w {sender_username} ")


# === 메인 루프 시작 === #
tk.mainloop()
