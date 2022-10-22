class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            nums[i] = None
            if remaining in nums:
                return [i, nums.index(remaining)]
