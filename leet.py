class Solution:
    def twoSum(self, nums = [2, 7, 11, 15], target = 9):
        Dict = {}
        for i in range(len(nums)):
            if target - nums[i] in Dict:
                return [i, Dict[target-nums[i]]]
            else:
                Dict[nums[i]] = i

solution = Solution()


