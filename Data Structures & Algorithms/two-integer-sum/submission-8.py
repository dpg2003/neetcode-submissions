class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            key = target - num
            if key in seen:
                return[seen[key],i]
            seen[num] = i