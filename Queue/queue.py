from typing import List


class Queue():
    def __init__(self) -> None:
        self.queue = list()

    def insert(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
    def remove(self):
        if len(self.queue) <= 0:
            print("The queue is empty")
        else:
            return self.queue.pop()
        

    def size(self):
        return len(self.queue)

# lets reference the Queue Object
TheQueue = Queue()
TheQueue.insert("Mon")
TheQueue.insert("Tue")
TheQueue.insert("Wed")
print(TheQueue.size())
print("Now lets pop some elements")
print(TheQueue.remove())
print(TheQueue.remove())
print(TheQueue.size())