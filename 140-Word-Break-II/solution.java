public class Solution {
    HashMap<String, List<String>> dp = new HashMap<>();
    
    public List<String> wordBreak(String s, Set<String> wordDict) {
        if(dp.containsKey(s))   return dp.get(s);
        
        List<String> result = new ArrayList<String>();

        for(int i = s.length() - 1; i > 0; --i){
            if(wordDict.contains(s.substring(i, s.length()))){
                List<String> next = wordBreak(s.substring(0, i), wordDict);
                if(next.size() > 0){
                    for(Iterator it = next.iterator(); it.hasNext();){
                        result.add(it.next() + " " + s.substring(i, s.length()));
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