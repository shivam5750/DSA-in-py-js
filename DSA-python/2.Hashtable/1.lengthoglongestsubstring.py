def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        map ={}
        start = maximum = 0
        for i in range(len(s)):
            if(s[i]  in map):
                start = map[s[i]] +1
            else:
                maximum = max(maximum, i-start+1)
                
            map[s[i]] =i
        return maximum
print(lengthOfLongestSubstring('pwwkew'))      