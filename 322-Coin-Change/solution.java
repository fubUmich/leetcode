public class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] min_coins = new int[amount + 1];
        for(int i = 1; i <= amount; ++i){
            min_coins[i] = Integer.MAX_VALUE;
            for(int coin_val : coins){
                if(i - coin_val >= 0 && min_coins[i - coin_val] >= 0){
                    min_coins[i] = Math.min(min_coins[i], min_coins[i-coin_val] + 1);
                }
            }
            if(min_coins[i] == Integer.MAX_VALUE)
                min_coins[i] = -1;
        }
        
        return min_coins[amount];
    }
}