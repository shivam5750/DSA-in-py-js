class Node {
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor(){
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }
  peek() {
    if(!this.length){
      return 'stack is empty'
    }
    return this.top
  }
  push(value){
    const newNode = new Node(value)
    if (!this.top){
      this.top = newNode
      this.bottom = newNode
      this.length++
    }else{
      let holdingPointer = this.top
      this.top = newNode
      this.top.next = holdingPointer
      this.length++
      
    }
  }
  pop(){
    if(!this.top){
      return 'no item to remove'
    }else if(this.length===1){
      this.top = null
      this.bottom = null
    }else{
      let holdingPointer = this.top.next
      this.top = holdingPointer
      this.length--
    }
    return this.top
  }
  //isEmpty
  isEmpty(){
    return !this.length ? true : false
  }
}

const myStack = new Stack();
myStack.peek()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.pop()
myStack.isEmpty()




//Discord
//Udemy
//google
