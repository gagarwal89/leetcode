class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1, row2, row3 = self.getRows()
        res = []
        for word in words:
            if self.processWord(word, row1) or self.processWord(word, row2) or self.processWord(word, row3):
                res.append(word)

        return res
    
    def processWord(self, word, row):
        for c in word:
            if not row.get(c.lower()):
                return False

        return True

    def getRows(self):
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        return self.convertRowToDict(row1), self.convertRowToDict(row2), self.convertRowToDict(row3)
    
    def convertRowToDict(self, row):
        res = dict()
        for c in row:
            res[c] = True

        return res