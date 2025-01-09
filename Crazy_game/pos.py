class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def to_list(self):
        return [self.x, self.y]

    @staticmethod
    def from_list(l):
        return Pos(l[0], l[1])