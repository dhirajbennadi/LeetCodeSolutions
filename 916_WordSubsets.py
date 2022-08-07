class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        def getFreq(element):
            tempMap = {}
            for i in range(0,26):
                tempMap[chr(ord('a') + i)] = 0
            for char in element:
                tempMap[char] += 1
            
            return tempMap
        
        map2 = {}
        mapTemp = {}
        for i in range(0,26):
            map2[chr(ord('a') + i)] = 0
        for element in words2:
            mapTemp = getFreq(element)
            
            for i in range(0,26):
                map2[chr(ord('a') + i)] = max(map2[chr(ord('a') + i)] , mapTemp[chr(ord('a') + i)])
        
        
        print(map2)
        result = []
        temp = []
        
        map1 = {}
        for i in range(0,26):
            map1[chr(ord('a') + i)] = 0
        
        for element in words1:
            for char in element:
                if char in map1:
                    map1[char] += 1
                else:
                    map1[char] = 1
            
            #print(map1)
            for key,val in map1.items():
                if key in map2:
                    #print(key,val, map2[key])
                    if val >= map2[key]:
                        #print(val)
                        temp.append(key)
            
            #print(temp)
            if len(temp) == len(map2):
                result.append(element)
            map1.clear()
            for i in range(0,26):
                map1[chr(ord('a') + i)] = 0
            temp.clear()
        
        
        #print(result)
        
        return result