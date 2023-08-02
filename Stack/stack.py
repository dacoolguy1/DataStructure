class stack():
    def __init__(self) :
        self.stack  = []

    def add(self, dataval):
        """add an item to the stack

        Args:
            dataval (_type_): the datavaraible to be added to the stack
        """
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        """Peak at the top of the stack to see the value there
        """
        return self.stack

    def remove(self):
        """Pop an item off
        """
        if len(self.stack) <= 0:
            print("The stack is empty")
        else:
            return self.stack.pop()

AStack = stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())
print("Stack when the pop operation has been performed")
print(AStack.remove())
print(AStack.remove())