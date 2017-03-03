class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def printAllVals(self):
        runner = list.head
        while(runner):
            print(runner.val)
            runner = runner.next
        return list

    def addBack(self, val):
        runner = list.head
        if (list.head != None):
            print list.head.val
        while(runner.next != None):
            print runner.next.val
            runner = runner.next
        runner.next = Node(val)
        print runner.next.val
        return list

    def addFront(self, val):
        print list.head.val
        temp = list.head
        new = Node(val)
        new.next = temp
        list.head = new
        print list.head.val, list.head.next.val
        return list

    def insertBefore(self, nextVal, val):
        pass


list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

print Node('Alice')
print Node('Chad')
