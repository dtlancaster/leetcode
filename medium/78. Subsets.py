class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]
        res = [[]]
        
        for num in nums:
            x = len(res)
            for i in range(x):
                n = res[i] + [num]
                res.append(n)
        
        return res
