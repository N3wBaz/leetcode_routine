class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Fist solution
        # idx = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             idx.append(i)
        #             idx.append(j)
        # return idx

        # Second solution
        # idx = [(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]
        # return idx[0]

        # Fastest solution
        my_dict = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in my_dict:
                return [my_dict[compliment], i]
            my_dict[num] = i
