class Solution {
    public int majorityElement(int[] nums) {
        int counter = 0;
        int val = 0;
        for(int i=0; i<nums.length; i++){
            val = nums[i];
            for (int j=0; j<nums.length; j++){
                if(val == nums[j]){
                    counter++;
                    if(counter>nums.length/2){
                        break;
                    }
                }
            }
        }
        return val;
    }
}
// public class Solution {
//     public int majorityElement(int[] nums) {
//         int n = nums.length;
//         for (int num : nums) {
//             int count = 0;
//             for (int i : nums) {
//                 if (i == num) {
//                     count++;
//                 }
//             }
//             if (count > n / 2) {
//                 return num;
//             }
//         }
//         return -1;
//     }
// }