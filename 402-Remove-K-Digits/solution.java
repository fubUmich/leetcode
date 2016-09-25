public class Solution {
    public String removeKdigits(String num, int k) {
        StringBuffer result = new StringBuffer();
        
        int index = 0;
        while(k > 0 && k + index < num.length()) {
            int minIndex = findMinInRange(num, index, index + k + 1);
            k -= (minIndex - index);
            index = minIndex + 1;
            result.append(num.charAt(minIndex));
        }
        if (k == 0)
            result.append(num.substring(index));
        
        int zeros = 0;
        for(; zeros < result.length(); ++zeros) {
            if(result.charAt(zeros) != '0') {
                break;
            }
        }
        if(zeros == result.length())
            return "0";
        else
            return result.toString().substring(zeros);
    }
    
    private int findMinInRange(String num, int start, int end) {
        if(start >= end) 
            return -1;
        
        int minIndex = start;
        for(int i = start + 1; i < end; ++i){
            if(num.charAt(i) < num.charAt(minIndex)) 
                minIndex = i;
        }
        return minIndex;
    }
}