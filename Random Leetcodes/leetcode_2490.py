class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        wordList = sentence.split(" ")
        if wordList[0][0] != wordList[-1][-1]:
            return False
        for i in range(0, len(wordList) - 1):
            if wordList[i][-1] != wordList[i+1][0]:
                return False
        return True

obj1 = Solution()
print(obj1.isCircularSentence("happy Leetcode"))