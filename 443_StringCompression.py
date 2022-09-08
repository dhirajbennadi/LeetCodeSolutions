class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count = 1
        output = []
        
        output.append(chars[0])
        
        for i in range(1,len(chars)):
        
            current = chars[i]
            prev = chars[i-1]
            
            if current == prev:
                count += 1
            else:
                if count > 1:
                    if count > 9:
                        numberCount = str(count)
                        for i in range(len(numberCount)):
                            output.append(numberCount[i])
                        # tensplace = count // 10
                        # unitsplace = count % 10
                        # output.append(str(tensplace))
                        # output.append(str(unitsplace))
                    else:
                        output.append(str(count))
                    count = 1
                
                output.append(current)
            
        
        if count > 1:
            if count > 9:
                numberCount = str(count)
                for i in range(len(numberCount)):
                    output.append(numberCount[i])
                # tensplace = count // 10
                # unitsplace = count % 10
                # output.append(str(tensplace))
                # output.append(str(unitsplace))
            else:
                output.append(str(count))
        
        print(len(output))
        print(output)
        
        for i in range(len(output)):
            chars[i] = output[i]
        
        return len(output)
            
    