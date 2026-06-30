class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # for size of nums 

        # counting element occurence 
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        # going through each element count and forming a hash/heap
        for n, v in count.items():
            freq[v].append(n)
        
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 

