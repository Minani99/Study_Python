class Stack:
    def __init__(root):
        root.list = []

    def push(root, item):
        root.list.append(item)

    def pop(root):
        return root.list.pop()


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.list)
print(stack.pop())
print(stack.list)
print(stack.pop())
print(stack.list)
print(stack.pop())
print(stack.list)
