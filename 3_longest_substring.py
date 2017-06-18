class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        maxSoFar = 1
        i=0
        j=0
        # Sliding window between i, j
        hash = dict()
        while i<len(s) and j<len(s):
            if hash.get(s[j]) is None:
                hash[s[j]] = j
                maxSoFar = max(maxSoFar, j+1-i)
                j += 1
            else:
                del hash[s[i]]
                i += 1
        return maxSoFar