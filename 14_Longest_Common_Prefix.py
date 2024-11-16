class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)

        count = 0
        for i, v in enumerate(strs[0]):
            if all(list(map(lambda x: x[i]==v, strs))):
                count += 1
            else:
                break   
        if count == 0:
            return ""
        return strs[0][:count]
                