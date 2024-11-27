class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = "#$%^&*()@,.!?:; '\"_=+-[]\\/\{\}`"
        for i in arr:
            s = s.replace(i, "")
        s = s.lower()
        return s == s[::-1]