class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def printlist(self):
        arr = []
        currentnode = self.head
        while currentnode:
            arr.append(currentnode.value)
            currentnode = currentnode.next
        return arr

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepand(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        if index == self.length:
            print(index)
            self.append(value)
        elif index == 0:
            print(index)
            self.prepand(value)
        else:
            newNode = Node(value)
            leader = self.traversetoindex(index - 1)
            holdingpointer = leader.next
            newNode.next = holdingpointer
            leader.next = newNode
            self.length += 1

    def remove(self, index):
        leader = self.traversetoindex(index - 1)
        holdingpointer = leader.next
        leader.next = holdingpointer.next
        self.length -= 1
        return self.printlist()

    def search(self, value):
        currentnode = self.head
        while (currentnode):
            if value == currentnode.value:
                return True
            currentnode = currentnode.next
        return False

    def traversetoindex(self, index):
        counter = 0
        current = self.head
        while (counter != index):
            current = current.next
            counter += 1
        return current

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = self.head.next
        while(second):
            third = second.next
            second.next = first
            first = second
            second = third
        self.head.next = None
        self.head = first
        return self.printlist()
    

mylinkedlist = Linkedlist(10)
mylinkedlist.append(16)
mylinkedlist.append(5)
mylinkedlist.prepand(20)
mylinkedlist.prepand(18)
mylinkedlist.insert(2, 30)
mylinkedlist.insert(6, 90)
# print(mylinkedlist.printlist())
print(mylinkedlist.remove(2))
print(mylinkedlist.search(5))
print(mylinkedlist.reverse())
print(mylinkedlist)
