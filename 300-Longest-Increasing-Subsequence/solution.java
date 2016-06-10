public class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> last_nums = new ArrayList<>();
        for(int num : nums){
            int index = binary_search(last_nums, num);
            if(index == last_nums.size())
                last_nums.add(num);
            else
                last_nums.set(index, num);
        }
        return last_nums.size();
    }
    
    private int binary_search(List<Integer> list, int num){
        int start = 0, end = list.size()-1, mid = (start + end) / 2;
        while(start <= end){
            if(list.get(mid) < num)
                start = mid + 1;
            else
                end = mid - 1;
            mid = (start + end) / 2;
        }
        return start;
    }
}