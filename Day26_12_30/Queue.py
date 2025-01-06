class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)
        # self.list.sort(reverse=True)
        # return self.list.pop()


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
