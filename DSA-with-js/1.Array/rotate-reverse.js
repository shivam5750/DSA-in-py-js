// rotate array by 1

function rotateArraybyOne(arr){
  for(let i=0; i< arr.length-1; i++){
    let hold =arr[i]
    arr[i] =arr[i+1]
    arr[i+1] = hold
  }
  return arr
}

rotateArraybyOne([1,2,3,4,5,8])


// reverse a array

function reverse(arr){
  start = 0
  high = arr.length-1
  while(start < high){
    let temp = arr[start]
    arr[start] = arr[high]
    arr[high] = temp

    start++
    high--
  }
  return arr
}

reverse([1,2,3,4,5])