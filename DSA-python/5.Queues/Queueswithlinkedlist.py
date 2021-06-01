class Node():
  def __init__(self,value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.last

  def  enqueue(self,value):
    newnode = Node(value)
    if not self.first:
      self.first = newnode
      self.last = newnode
    else:
      self.last.next = newnode
      self.last = newnode
    self.length+=1
    return self.last.value

  def dequeue(self):
    if not self.first:
      return 'empty'
    if self.length==1:
      self.first= None
      self.last = None
    else:
      holdingpointer = self.first.value
      self.first = self.first.next
    self.length-=1
    return holdingpointer
  
myqueue = Queue()
myqueue.enqueue('matt')
myqueue.enqueue('harry')
myqueue.enqueue('jiren')
print(myqueue.enqueue('top'))
print(myqueue.dequeue())
print(dir(myqueue))



