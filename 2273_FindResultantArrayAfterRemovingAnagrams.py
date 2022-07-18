class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        '''Brute Force'''
        left = 0
        right = 1
        wordslen = len(words)
        
        itemsRemove = []
        
        while right < wordslen:
            
            d1map = {}
            d2map = {}
            d1map = self.calculateHashmap(words[left])
            d2map = self.calculateHashmap(words[right])
            
            if d1map == d2map:
                itemsRemove.append(right)
            
            right += 1
            left += 1
        
        result = []
        for index,elements in enumerate(words):
            if index in itemsRemove:
                continue
            else:
                result.append(words[index])
            
        return result
    
    
    def calculateHashmap(self, words: List[str]) -> dict:
        
        dummy = {}
        
        for i in range(26):
            dummy[chr(ord('a') + i)] = 0
        
        for i in range(len(words)):
            dummy[words[i]] += 1
        
        return dummy