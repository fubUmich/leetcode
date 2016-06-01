public class Solution {
    
    HashMap<String, List<String>> dp = new HashMap<>();
    public List<String> wordBreak(String s, Set<String> wordDict) {
        
        if(dp.containsKey(s))   return dp.get(s);
        
        List<String> result = new ArrayList<String>();
        for(int i = s.length() - 1; i >= 0; --i){
            if(wordDict.contains(s.substring(i, s.length())))
                break;
            else if(i == 0)
                return result;
        }
        
        for(int i = 1; i < s.length(); ++i){
            if(wordDict.contains(s.substring(0, i))){
                List<String> next = wordBreak(s.substring(i, s.length()), wordDict);
                if(next.size() > 0){
                    for(Iterator it = next.iterator(); it.hasNext();){
                        result.add(s.substring(0, i) + " " + it.next());
                    }
                }
            }
        }
        if(wordDict.contains(s))
            result.add(s);
        
        dp.put(s, result);
        return result;
    }
}