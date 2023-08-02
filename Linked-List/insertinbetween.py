"""Inserting a new node at the end in between the Linked List"""
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
    
    def InBetween(self, middle_node, newdata):
        NewNode = Node(newdata)
       # if the list is empty create a new list.
        if middle_node is None:
            print("The middle node is empty")
        
        # middle_node.nextval = NewNode.nextval 
        # NewNode.nextval = middle_node
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
          # lets transverse to the last node
                
            # print(self.dataval[-1])
        # NewNode.dataval = NewNode # now our head is the new node


linked_list = SLinkedList()  #referencing the single linked list and Creating an instance of the class
linked_list.headval = Node("Mon")  # head of the list is Mon that is the first node
e2 = Node("Tue")
e3 = Node("Wed")

# lets Link first node to the second node:
linked_list.headval.nextval = e2

# LEts link second node with the third node
e2.nextval = e3
# linked_list.AtEnd("Sun")
linked_list.InBetween(linked_list.headval.nextval,"Fri")

linked_list.listprint()