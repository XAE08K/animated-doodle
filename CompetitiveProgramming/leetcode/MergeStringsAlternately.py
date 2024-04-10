class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=''
        iter=min(len(word1),len(word2))
        for i in range(iter):
            new+=word1[i]
            new+=word2[i]

        if len(word2)>len(word1):
            new+=word2[iter:]
        else:
            new+=word1[iter:]
        return new
        