# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


def threeSum(self, nums: List[int]) -> List[List[int]]:
    count = Counter(nums)
    nums = list(count.keys())
    
    ans = set()
    
    if count[0] >= 3: 
        ans.add((0, 0, 0))
    positive, negative = [x for x in nums if x > 0], [x for x in nums if x < 0]
    print(positive, negative)
    for a in negative:
        for b in positive:
            seen = -(a + b)
            if seen in count and ((seen != a and seen != b) or count[seen] > 1):
                ans.add(tuple(sorted([a, b, seen])))
    return ans