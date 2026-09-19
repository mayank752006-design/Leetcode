import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1, r = n - 1;

            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];
                if (s < 0) {
                    l++;
                } else if (s > 0) {
                    r--;
                } else {
                    ans.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    while (l < r) {
                        if (nums[l] == nums[l + 1]){
                            l++;
                        } else {break;}
                    }

                    while (l > r) {
                        if (nums[r] == nums[r - 1]) {
                            r--;
                        } else{break;}
                    }
                    l++;
                    r--;
                }
            }
        }
        return ans;
    }
}