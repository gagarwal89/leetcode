class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=0
        s = list(s)
        while j < len(s):
            if s[j] == ' ':
                # Reverse i to j-1th index
                s[i:j] = s[i:j][::-1]
                i = j+1
            j += 1
            if j == len(s):
                s[i:j] = s[i:j][::-1]
        return ''.join(s)