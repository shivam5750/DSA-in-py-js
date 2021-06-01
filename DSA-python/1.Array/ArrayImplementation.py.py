class MyArray():
  def __init__(self):
    self.length = 0
    self.data ={}
  
  def __str__(self):
    return str(self.__dict__)
  
  def get(self, index):
    return self.data[index]
  
  def append(self, items):
    self.data[self.length] = items
    self.length +=1
    return self.length
  
  def pop(self):
    lastItem = self.data[self.length-1]
    del(self.data[self.length -1])
    self.length -=1
    return lastItem
  
  def remove(self, index):
    item = self.data[index]
    self.shiftItems(index)
    return item
  
  def shiftItems(self, index):
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]
    del(self.data[self.length -1])
    self.length-=1

  def insert(self, index, newItem):
    self.shiftItems2(index, newItem)
    return newItem
  
  def shiftItems2(self, index, newItem):
    length = self.length
    for i in range(index, length):
       self.data[length] = self.data[length-1]
       length-=1
    self.data[index] = newItem
    self.length +=1

    



Array = MyArray()
Array.append('mango')
Array.append('apple')
Array.append('grapes')
Array.append('pineapple')
Array.append('Guava')
Array.pop()
Array.remove(2)
Array.insert(2, 'banana')
print(Array)

