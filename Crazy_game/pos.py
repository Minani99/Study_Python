class Pos:
    def __init__(root, x, y):
        root.x = x
        root.y = y

    def __eq__(root, other):
        return root.x == other.x and root.y == other.y

    def __hash__(root):
        return hash((root.x, root.y))

    def __str__(root):
        return f"({root.x}, {root.y})"

    def __repr__(root):
        return root.__str__()

    def __add__(root, other):
        return Pos(root.x + other.x, root.y + other.y)

    def to_list(root):
        return [root.x, root.y]

    @staticmethod
    def from_list(l):
        return Pos(l[0], l[1])