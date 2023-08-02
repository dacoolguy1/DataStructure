"""Undestanding Linked List"""
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print(printval)
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


linked_list = SLinkedList()  #referencing the single linked list and Creating an instance of the class
linked_list.headval = Node("Mon")  # head of the list is Mon that is the first node
e2 = Node("Tue")
e3 = Node("Wed")

# lets Link first node to the second node:
linked_list.headval.nextval = e2

# LEts link second node with the third node
e2.nextval = e3

linked_list.listprint()