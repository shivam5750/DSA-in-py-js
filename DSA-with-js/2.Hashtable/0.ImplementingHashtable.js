class HashTable {
  constructor(size){
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i =0; i < key.length; i++){
        hash = (hash + key.charCodeAt(i) * i) % this.data.length
    }
    return hash;
  }

  set(key, value){
    let address = this._hash(key)
    if(!this.data[address]){
      this.data[address] = []
    }
      this.data[address].push([key, value])
       return this.data
  }

  get(key){
    let address = this._hash(key)
    const currentBucket = this.data[address]
    console.log(currentBucket)
    if(currentBucket){
      for(let i=0 ; i<currentBucket.length; i++){
        if(currentBucket[i][0]===key){
          return currentBucket[i][1]
        }
      }
    }
    return undefined
  }

  keys(){
    let keyArray =[]
    for(let i =0; i < this.data.length; i++){
      if(this.data[i]){
        keyArray.push(this.data[i][0][0])
      }
    }
    return keyArray
  }


  values(){
      let valueArray =[]
      for(let i =0; i < this.data.length; i++){
        if(this.data[i]){
          valueArray.push(this.data[i][0][1])
        }
      }
      return valueArray
    }
}
const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 345)
myHashTable.set('oranges', 45)
myHashTable.set('banana', 945)
myHashTable.get('apples')
myHashTable.keys()
myHashTable.values()