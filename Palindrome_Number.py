class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # First
        # x = str(x)
        # for i, j in zip(x, x[::-1]):
        #     if i != j:
        #         return False
        #         break
        # return True

        # Faster
        n = x
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return reversed_x == n

        # Fastest
        # num = str(x)
        # if (num == num [::-1]):
        #     return True
        # else: 
        #     return False