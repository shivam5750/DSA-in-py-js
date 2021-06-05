// to find the scond largest elememt in an array

// naive approach

function largest(arr){
  let largest = 0
  for(let i=0; i<arr.length; i++){
    if(arr[i]>largest){
      largest = arr[i]
    }
  }
  return largest
}

function secondLargest(arr){
  let second = 0
  for(let i=0; i<arr.length;i++){
    if(arr[i]!==largest(arr)){
      if(second === arr[i]){
        return second
      }
      if(arr[i]>second){
        second = arr[i]
      }
    }
  }
  return second
}

// secondLargest([2,3,6,7,9,1,7])

// Effiicient approach

function secondLargestNum(arr){
  let n = arr.length
  let largest = 0
  let second = 0
  for(let i=1; i<n;i++){
    if(arr[i]>arr[largest]){
      second = largest
      largest = arr[i]
    }else if(arr[i]!== arr[largest]){
      if(second === 0 || arr[i]>arr[second]){
        second = i
      }
    }
  }
  return arr[second]
}

secondLargestNum([2,3,6,7,9,8,7,6,8])