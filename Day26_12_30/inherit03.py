class CustomException(Exception):
    def __init__(root,message,value):
        super().__init__(root)
        root.message = message
        root.value = value

    def __str__(root):
        return root.message

    def print(root):
        print("오류정보")
        print("메시지: ",root.message)
        print("값", root.value)


try:
    raise CustomException("뭐 꼽냐",273)
except CustomException as e:
    e.print()
