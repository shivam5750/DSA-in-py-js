// Given a string s, find the length of the longest substring without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0

//Answer in Js

var lengthOfLongestSubstring =(s)=> {
    seen ={}
    start = max = 0
    for(let i=0; i<s.length; i++){
        if((seen[s[i]]!==undefined) &&(start <= seen[s[i]])){
            start = seen[s[i]]+1
        }else{
            max = Math.max(max, i-start+1)
        }
        seen[s[i]] =i
    }
    return max
};