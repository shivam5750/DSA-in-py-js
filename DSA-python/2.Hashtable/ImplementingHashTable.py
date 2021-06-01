class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] *self.size
        
    
    def __hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i)%self.size
        return hash
    
    def set(self,key,value):
        address= self.__hash(key)
        if(not self.data[address]):
            self.data[address] =[]
        self.data[address].append([key, value])
        return self.data
    
    def get(self,key):
        address = self.__hash(key)
        currentBucket = self.data[address]
        if(currentBucket):
            for i in currentBucket:
                print(i)
                if i[0] ==key:
                    return i[1]
                else:
                    return None
    def keys(self):
        keyarray =[]
        for i in self.data:
            if(i):
                keyarray.append(i[0][0])
        return keyarray
    
    def values(self):
        valuearray =[]
        for i in self.data:
            if(i):
                valuearray.append(i[0][1])
        return valuearray
                

myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 3000)
myHashTable.set('oranges', 500)
print(myHashTable.set('banana', 10))
print(myHashTable.get('apples'))
print(myHashTable.keys())
print(myHashTable.values())