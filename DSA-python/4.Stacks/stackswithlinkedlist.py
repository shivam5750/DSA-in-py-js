class Node():
  def __init__(self,value):
    self.value = value
    self.next = None
  
  def __str__(self):
    return str(self.__dict__)

class Stacks:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def __str__(self):
    return str(self.__dict__)
  

  def peek(self):
    if not self.top:
      return 'stack is empty'
    return self.top

  def push(self,value):
    newnode = Node(value)
    if not self.top:
      self.top = newnode
      self.bottom = newnode
    else:
      holdingpointer = self.top
      self.top = newnode
      self.top.next = holdingpointer
    return self.top

  def pop(self):
    if not self.top:
      return 'empty'
    if self.length==1:
      self.top= None
      self.bottom = None
    else:
      holdingpointer = self.top.next
      self.top = holdingpointer
    return self.top


mystacks = Stacks()
mystacks.push('google')
mystacks.push('udemy')
mystacks.push('discord')
print(mystacks.pop())
print(mystacks.pop())
print(mystacks.pop())

  
# //Discord
# //Udemy
# //google