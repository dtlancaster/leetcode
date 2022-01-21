class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            if target - value in dict:
                return [dict[target - value], index]
            else:
                dict[value] = index
