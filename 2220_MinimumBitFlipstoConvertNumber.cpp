class Solution {
public:
    int minBitFlips(int start, int goal) {
        
        //Bitwise Operation
        int countBits = 0;
        int resultBits = start ^ goal;
        
        while(resultBits)
        {
            /*Kernighan Algorithm*/
            resultBits = resultBits & (resultBits - 1);
            countBits++;
        }
        
        return countBits;
        
        //Brute Force
        int count = 0;
        int checkValb = 0;
        int checkVala = 0;
        int result = 0;
        int val = 1;
        
        while(count < 31)
        {
           checkValb = goal & val; 
           checkVala = start & val;
           
           //cout << checkValb << " " << checkVala << endl;
           
           if(checkValb != checkVala)
           {
               result++;
           }
           
           count++;
           val = val << 1;
           
           
           
        }
        
        return result;
    }
};