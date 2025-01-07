class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def set_name(self, new_name):
        self.__name = new_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


p1 = Person("김동현", 28)
p1.name = "박민환"
