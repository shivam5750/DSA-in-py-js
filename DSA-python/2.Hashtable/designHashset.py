class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data= [None]*2000000
    
    def __hash(self,key):
        return hash(key)
        

    def add(self, key: int) -> None:
        address = self.__hash(key)
        currentBucket = self.data[address]
        print(currentBucket)
        if(currentBucket):
            for i in currentBucket:
                print(i)
                if i == key:
                    break
            
        elif(not self.data[address]):
            self.data[address]=[]
            self.data[address].append(key)

        
        

    def remove(self, key: int) -> None:
        pass
        address = self.__hash(key)
        currentBucket = self.data[address]
        if(currentBucket):
            for i in currentBucket:
                if i == key:
                    currentBucket.remove(i)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        address = self.__hash(key)
        currentBucket = self.data[address]
        if(currentBucket):
            for i in currentBucket:
                if i == key:
                    return True
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)