class Stacks:
  def __init__(self):
    self.array = []

  def __str__(self):
    return str(self.__dict__)
  

  def peek(self):
    return self.array[len(self.array)-1];

  def push(self,value):
    self.array.append(value)
    return self.array

  def pop(self):
    self.array.pop()
    return self.array


mystacks = Stacks()
mystacks.push('google')
mystacks.push('udemy')
mystacks.push('discord')
print(mystacks.push('youtube'))
mystacks.pop()
print(mystacks.pop())

  
# //Discord
# //Udemy
# //google