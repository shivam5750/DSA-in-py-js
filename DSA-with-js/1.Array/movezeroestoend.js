function moveZeroesToEnd(arr){
  const n = arr.length
  let count=0
  for(let i=0; i< n; i++){
    if(arr[i]!==0){
      let holdingElement = arr[count]
      arr[count] = arr[i]
      arr[i] = holdingElement
      count++
    }
  }
  return count
}

moveZeroesToEnd([8,5,0,0,10,0,20,0])