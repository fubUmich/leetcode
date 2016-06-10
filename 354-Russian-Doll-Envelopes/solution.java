public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, new Comparator<int[]>(){
            @Override
            public int compare(int[] arr1, int[] arr2){
                if(arr2[0] == arr1[0])
                    return arr2[1] - arr1[1];
                return arr1[0] - arr2[0];
            }
        });
        
        
        
        List<Integer> dp = new ArrayList<Integer>();
        for(int[] env : envelopes){
            int index = binary_search(dp, env[1]);
            if(index == dp.size()){
                dp.add(env[1]);
            }
            else
                dp.set(index, env[1]);
        }
        
        return dp.size();
    }
    
    private int binary_search(List<Integer> list, int target){
        int start = 0, end = list.size() - 1, mid = start + (end - start) / 2;
        while(start <= end){
            if(list.get(mid) < target)
                start = mid + 1;
            else
                end = mid - 1;
            mid = start + (end - start) / 2;
        }
        return start;
    }
}

