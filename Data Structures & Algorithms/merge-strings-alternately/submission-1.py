class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            newString += word1[i] + word2[i]
            
        
        if len1 < len2:
            newString += word2[len1::]
        elif len2 < len1:
            newString += word1[len2::]

        return newString