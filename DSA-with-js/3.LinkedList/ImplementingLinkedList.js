// Create the below linked list:
// myLinkedList = {
//   head: {
//     value: 10
//     next: {
//       value: 5
//       next: {
//         value: 16
//         next: null
//       }
//     }
//   }
// };

class Node{
  constructor(value){
    this.value=value,
    this.next = null
  }
}
class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null
    };
    this.tail = this.head;
    this.length = 1;
  }
  append(value) {
    const newNode = new Node(value)
    this.tail.next = newNode
    this.tail = newNode
    this.length++
    return this
  }

  prepand(value){
    const newNode = new Node(value)
    newNode.next = this.head
    this.head = newNode
    this.length++
    return this
  }

  // Just to make linked list look more clear 
  printList(){
    const array = []
    let currentBucket = this.head
    while(currentBucket!== null){
      array.push(currentBucket.value)
      currentBucket= currentBucket.next
    }
    return array
  }

  insert(index, value){
    if(index === 0){
      this.prepand(value)
      return this

    }else if(index >= this.length){
       this.append(value)
       return this
    }
    const newNode = new Node(value)
    // leader ->prior node to newNode
    // holdingNode-> node after the newNode
    const leader = this.traverseToIndex(index-1)
    const holdingNode = leader.next
    leader.next = newNode
    newNode.next = holdingNode
    this.length++
    return this
  }

  remove(index){
    let leader = this.traverseToIndex(index-1)
    let unwantedNodeNext = leader.next
    leader.next = unwantedNodeNext.next
    this.length--
    return this
  }

  search(value){
    let currentNode =this.head
    while(currentNode.next !== null){
      if(value === currentNode.value){
        return true
      }else{
        return false
      }
      currentNode = currentNode.next
    }
  }


  traverseToIndex(index){
    let counter =0
    let currentNode = this.head
    while(counter < index){
      currentNode = currentNode.next
      counter++
      
    }
    return currentNode

  }
}

let myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepand(13);
myLinkedList.prepand(20);
myLinkedList.append(17);
myLinkedList.insert(2,21)
myLinkedList.insert(5,90)
myLinkedList.remove(2)
console.log(myLinkedList.search(21))
myLinkedList.printList()



