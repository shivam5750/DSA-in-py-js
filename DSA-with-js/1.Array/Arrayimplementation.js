class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }
  get(index){
    return this.data[index] 
  }

  push(value){
    this.data[this.length] = value
    this.length++
    return this
  }

  pop(){
    let lastItem = this.data[this.length-1]
    delete this.data[this.length-1]
    this.length--
    return lastItem
  }

  insert(index, value){
    this.shiftItems1(index,value)
    return this
  }

  shiftItems1(index,value){
    let length = this.length
    let holding = this.data[index]
    for(let i=index; i<length; i++){
     const nextData =  this.data[i+1]
     this.data[i+1] = holding
     holding = nextData

    }
    this.data[index] = value
    this.length++
  }

  delete(index){
    const item = this.data[this.length-1]
    this.shiftItems2(index)
  }

  shiftItems2(index){
    for(let i=index; i<this.length-1; i++){
      this.data[i] = this.data[i+1]

    }
    delete this.data[this.length-1]
    this.length--
    return this
  }
 
}

const myArray = new MyArray();
myArray.push('hi');
myArray.push('you');
myArray.push('!');
myArray.push('jacon')
myArray.get(1)
// myArray.pop();
myArray.insert(1,'hello')
myArray.delete(1)
myArray


