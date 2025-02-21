import tkinter as tk

# 메인 프레임(메인 윈도우) 생성
main = tk.Tk()
main.title("123")

# 라벨 위젯 생성
label = tk.Label(main, text="기본라벨")
label.pack()  # pack을 통한 화면의 위젯 배치


# 버튼 클릭 이벤트 처리 함수
def on_button_click():
    label.config(text="클릭되었음")  # 라벨의 텍스트 변경


# 버튼 위젯 생성 및 이벤트 바인딩
button = tk.Button(main, text="클릭", command=on_button_click)
# command에는 함수를 바인딩해준다(함수 호출 아님)
button.pack()

# Entry(한 줄 입력받는 텍스트 박스)
e = tk.Entry(main)  # 입력 필드 생성
e.pack()


# Entry에 입력된 텍스트를 가져와 라벨에 표시하는 함수
def show_entry():
    user_input = e.get()  # Entry 필드에서 입력값 가져오기
    label.config(text=f'입력된 텍스트: {user_input}')  # 라벨 텍스트 변경


# 버튼 생성 및 show_entry 함수와 이벤트 바인딩
button = tk.Button(main, text='입력값 보기', command=show_entry)
button.pack()

# Text (여러 줄 입력 가능한 텍스트 박스)
text_box = tk.Text(main, height=5, width=30)  # 텍스트 위젯 생성
text_box.pack()  # 여러 줄 텍스트 입력받을 수 있는 텍스트 박스


# Text 위젯에서 입력된 내용을 가져와 라벨에 표시하는 함수
def show_text():
    text_content = text_box.get("1.0", "end-1c")  # 텍스트 박스의 값을 가져옴
    # get(start, end) 메서드 사용
    # start: 텍스트 가져오고자 하는 시작 위치 ("1.0" → 1번째 줄의 0번째 문자)
    # end: 텍스트 가져오고자 하는 끝 위치 ("end-1c" → 마지막 줄의 마지막 문자 앞까지)
    label.config(text=f'입력된 텍스트: {text_content}')  # 라벨 텍스트 변경


# 버튼 생성 및 show_text 함수와 이벤트 바인딩
button = tk.Button(main, text='텍스트 보기', command=show_text)
button.pack()

# Checkbutton 위젯 (체크박스 생성)
check_var = tk.BooleanVar()  # 체크 여부를 저장할 변수 TF값으로 체크 박스의 상태 관리
checkbutton = tk.Checkbutton(main, text='체크 여부', variable=check_var)
# variable : check_var라는 boolvar 변수
checkbutton.pack()


def check_status():
    if check_var.get():
        label.config(text='체크박스 선택됨')
    else:
        label.config(text='선택 풀림')


button = tk.Button(main, text='TF변환 체크', command=check_status)
button.pack()

selected_option = tk.StringVar()  # 선택 값을 저장할 변수 선언


def show_radio_selection():
    label.config(text=f'라디오선택옵션:{selected_option.get()}')


radiobutton1 = tk.Radiobutton(main, text='옵션1', variable=selected_option, value='1')
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(main, text='옵션1', variable=selected_option, value='2')
radiobutton2.pack()
# radiobutton 1과 2의
button = tk.Button(main, text='선택확인', command=show_radio_selection)
button.pack()

# 리스트박스 위젯
listbox = tk.Listbox(main)  # 여러 항목을 선택할 수 있는 리스트 박스
listbox.pack()

for item in ['항목1', '항목2', '항목3']:
    listbox.insert(tk.END, item)


def show_select_item():
    selected_item = listbox.get(listbox.curselection())
    label.config(text=f'선택된 항목:{selected_item}')


button = tk.Button(main, text='선택된항목보기', command=show_select_item)
button.pack()

# scale위젯
# 사용자가 슬라이더를 조작하여 값을 선택하는 위젯

scale = tk.Scale(main, font=0, to=100, orient=tk.HORIZONTAL)
scale.pack()


def show_scale_value():
    value = scale.get()  # 슬라이더가 어떤 값인지 조회
    label.config(text=f'슬라이더 값:{value}')


button = tk.Button(main, text='슬라이더값확인', command=show_scale_value)
button.pack()

spinbox = tk.Spinbox(main, from_=1, to=10)  # 1~10 사이의 값 선택 가능한 스핀박스 생성
spinbox.pack()


def show_spinbox_value():
    value = spinbox.get()
    label.config(text=f'spinbox값:{value}')


button = tk.Button(main, text='spinbox값 보기', command=show_spinbox_value)
button.pack()

# 스크롤바 위젯 생성
# 스크롤바는 텍스트나 리스트 박스에 내용이 width height 넘어갈떄 처리
scrollbar = tk.Scrollbar(main)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # 스크롤바를 오른쪽에 세로로 배치

listbox = tk.Listbox(main, yscrollcommand=scrollbar.set)
# 리스트박스의 생성 및 스크롤바와 바인딩
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# 리스트박스를 왼쪽에 배치하고 크기 조정

for item in range(50):
    listbox.insert(tk.END, f'항목{item + 1}')

scrollbar.config(command=listbox.yview)


# 스크롤바와 리스트박스를 바인딩해서 스크롤 가능하게 연결

# menu 위젯
# 메뉴 위젯은 애플리케이션 메뉴 만들때 사용, 상단 메뉴바, 컨텍스트 메뉴 등

def new_file():
    label.config(text='새 파일 생성')


def save_file():
    label.config(text='파일 저장')


def open_file():
    label.config(text='파일 열기')


menu_bar = tk.Menu(main)  # 메뉴 바 위젯 생성

file_menu = tk.Menu(menu_bar, tearoff=0)  # 파일 메뉴 생성(tearoff=0: 분리되는 메뉴 방지)
# tearoff=1 메누의 상단에 작은 점선 라인 생김
# 점선 라인 클릭시 메뉴 분리(떼어내기) 가능

# tearoff=0
# 메뉴에서 점선사라짐 메뉴 분리 안됨
# 항상 한곳에서 사용되도록 강제

file_menu.add_command(label='새로만들기', command=new_file)  # 새로만들기 메뉴
file_menu.add_command(label='열기', command=open_file)
file_menu.add_command(label='저장', command=save_file)
menu_bar.add_cascade(label='파일', menu=file_menu)  # 파일 메뉴를 메뉴바에 추가
main.config(menu=menu_bar)  # 메뉴바를 메인창에 추가


# Toplevel 탑레벨은 새로운 창을 생성하는 위젯
# 메인 창 외에 추가적인 대화상자나 새 창을 띄울때 사용

def open_new_window():
    new_window = tk.Toplevel(main)
    new_window.title('새 창')
    new_window.geometry('200x150')
    label_in_new_window = tk.Label(new_window, text='새창라벨')
    label_in_new_window.pack()


# button = tk.Button(main, text='새창열기', command=open_new_window)
# button.pack()
#
# # canvas위젯
# # 캔버스 위젯튼 그림그리거나 도형그리거나 그래픽 작업 할때 사용
# canvas = tk.Canvas(main, width=400, height=300, bg='white')
# canvas.pack()
#
# # canvas.create_rectangle(50,50,150,150,file='blue')
# canvas.create_oval(200, 50, 300, 150, fill='red')
# canvas.create_line(30, 200, 350, 200, fill='green', width=3)
#
# # message위젯
# # 메시지 위젯은 긴 텍스트를 자동으로 줄바꿈 해주는 위젯
#
#
# # 일반적인 label 위젯과 비슷하지만 긴 텍스트 처리에 적합하다
#
# message = tk.Message(main, text='자동줄바꿈되는 텍스트 123123 입니다 긴 텍스트 처리시 적합하다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ'
#                      , width=300)
# message.pack()

# tkinter로 개발하는 GUI 프로세스는 1개당 1개의 mainloop()가 있어야 함
main.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# root=tk.Tk()
# root.title('ttk버튼')
# def on_button_click():
#     print("button clicked")
#
# button=ttk.Button(root,text='click',command=on_button_click)
# button.pack(padx=10,pady=10)
#
# root.mainloop()