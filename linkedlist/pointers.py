class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def print(self):
        print("------")
        p1 = self.headval
        while (p1 != None):
            print(p1.dataval)
            p1 = p1.next

    def reverseList(self):
        head = self.headval
        prev = None
        curr = head
        if head == None or head.next == None:
            return
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.headval = prev
        return 

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.next = e2

# Link second Node to third node
e2.next = e3
list1.print()
list1.reverseList()
list1.print()