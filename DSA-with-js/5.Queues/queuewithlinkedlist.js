class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor(){
    this.first = null;
    this.last = null;
    this.length = 0;
  }
  peek() {
    return this.last
  }
  enqueue(value){
    const newNode = new Node(value)
    if(!this.first){
      this.first= newNode;
      this.last = newNode
    }else{
      this.last.next = newNode
      this.last = newNode
    }
    this.length++
    return this
  }
  dequeue(){
    if(!this.first){
      return
    }
    if(this.length ===1){
      this.first =null
      this.last = null
    }else{
      let holdingPointer = this.first.next
      this.first = holdingPointer
    }
    this.length--
    return this
  }
  //isEmpty;
}

const myQueue = new Queue();
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')
myQueue.dequeue()
//Joy
//Matt
//Pavel
//Samir

