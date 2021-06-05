//you are given two unsorted array merge them and also sort them in proper way without using any inbuilt methods of javascript

function mergeSortedArray(array1, array2){
	if(!array1.length){
		return array2
	}
	if(!array2.length){
		return array1
	}

	const mergedArray = []
	array1Item = array1[0]
	array2Item = array2[0]
	i=1
	j=1

	while(array1Item || array2Item){
		if(array2Item=== undefined || array1Item< array2Item){
			mergedArray.push(array1Item)
			array1Item = array1[i]
			i++
		}else{
			mergedArray.push(array2Item)
			array2Item = array2[j]
			j++
		}
	}
	return mergedArray
}

mergeSortedArray([0,3,4,31],[4,6,30])