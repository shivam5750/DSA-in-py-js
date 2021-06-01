class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


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
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self.printlist()

    def prepand(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self.printlist()

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
            newNode.prev = leader
            holdingpointer.prev = newNode
            self.length += 1
        return self.printlist()

    def remove(self, index):
        leader = self.traversetoindex(index - 1)
        holdingpointer = leader.next
        leader.next = holdingpointer.next
        holdingpointer.prev = leader
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
