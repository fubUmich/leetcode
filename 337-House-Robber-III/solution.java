/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int rob(TreeNode root) {
        int[] maxRob = robSubTree(root);
        return Math.max(maxRob[0], maxRob[1]);
    }
    
    private int[] robSubTree(TreeNode root) {
        // return: [max rob robbing current Node, max rob not robbing current Node]
        if(root == null) 
            return new int[] {0, 0};
        
        int[] result = new int[2];
        int[] left = robSubTree(root.left);
        int[] right = robSubTree(root.right);
        result[0] = root.val + left[1] + right[1];
        result[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return result;
    }
}