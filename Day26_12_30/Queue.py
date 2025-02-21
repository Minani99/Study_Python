class Queue:
    def __init__():
        .list = []

    def enqueue(root, item):
        root.list.append(item)

    def dequeue(root):
        return root.list.pop(0)
        # root.list.sort(reverse=True)
        # return root.list.pop()


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
