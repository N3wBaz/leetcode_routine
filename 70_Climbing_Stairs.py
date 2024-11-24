# Fastest
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return n
        a = b = 1
        
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# My solution
class Solution(object):
    def factor(self, n):
        acc = 1
        for i in range(n):
            acc *= i + 1
        return acc
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        acc = 0
        for i in range(n):
            twice = 2 * i
            single = n - twice
            nums = i + single
            acc += int(self.factor(nums) / (self.factor(nums - i) * self.factor(i)))
        return acc