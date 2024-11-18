class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = set()
        l.update(nums)
        l = list(l)
        l.sort()
        for i in range(len(l)):
            if nums[i] == l[i]:
                continue
            else:
                nums[i] = l[i]
        return len(l)