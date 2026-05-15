class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n = nums.length; 
        int res=0;
        int count = 0;
        for ( int i = 0; i < n; i++){
            if (nums[i] == 1){
                count ++;
            }
            else{
                res= Math.max(res, count);            // Math.max(a, b) returns the larger of the two values
                count =0;
            }
        }
                    res = Math.max(res,count);
                    return res;
    }
}