package com.shine.data.leetcode;

import java.util.HashMap;
import java.util.Map;

public class L_2958 {

    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        int ans = 0;
        int l = 0, r = 0;
        while (r < nums.length) {
            if (freq.getOrDefault(nums[r], 0) < k) {
                freq.compute(nums[r], (_, value) -> value == null ? 1 : value + 1);
                r++;
            } else {
                freq.compute(nums[l], (_, value) -> value - 1);
                l++;
            }
            ans = Math.max(ans, r - l);
        }
        return ans;
    }
}
