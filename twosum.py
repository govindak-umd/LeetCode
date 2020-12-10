class Solution:

    def twoSum(self, nums, target):
        count = 0
        for num in nums:
            for idx in range(len(nums)):
                if idx != count:
                    if nums[idx] + num == target:
                        if idx < count:
                            return [idx,count]
                        else:
                            return [count,idx]
            count += 1