class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 : Hashmap solution 
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i 
        return true
        
        # solution 2 : Brute force
        i, j = 0, 0 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

        