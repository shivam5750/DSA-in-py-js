// #unique no of occurance

// Share
// Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

// Example 1:

// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
// Example 2:

// Input: arr = [1,2]
// Output: false
// Example 3:

// Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
// Output: true
 

// Constraints:

// 1 <= arr.length <= 1000
// -1000 <= arr[i] <= 1000


var uniqueOccurrences = function(arr) {
    occ = {}
    for(let i of arr){
        if(occ[i]){
            occ[i] +=1
        }else{
            occ[i] =1
        }
    } 
    
    if(new Set(Object.values(occ)).size ===Object.values(occ).length ){
        return true
    }
    return false
    
    
};

// The other way- same with new syntax
var uniqueOccurrences = function(arr) {

    const counter = new Map();
    
    for (let a of arr)
        counter.set(a, (counter.get(a) ?? 0) + 1);
    
    const occurrences = new Set(counter.values());
    
    return counter.size === occurrences.size;
};