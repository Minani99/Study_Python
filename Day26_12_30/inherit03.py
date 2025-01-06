class CustomException(Exception):
    def __init__(self,message,value):
        super().__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("오류정보")
        print("메시지: ",self.message)
        print("값", self.value)


try:
    raise CustomException("뭐 꼽냐",273)
except CustomException as e:
    e.print()
