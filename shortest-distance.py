


class Solution:

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d1 = -1
        d2 = -1
        
        mini = len(wordsDict) + 1
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                d1 = i
            
            if wordsDict[i] == word2:
                d2 = i
            
            
            if d1 != -1 and d2 != -1 :
                mini = min(mini, abs(d1 - d2))
            
        return mini