package com.shine.data.leetcode;

import java.util.Arrays;

public class L_875 {


    public int minEatingSpeed(int[] piles, int h) {
        int n = piles.length;
        Arrays.sort(piles);
        int ans = piles[n - 1] + 1;
        int left = 1;
        int right = piles[n - 1];
        while (left <= right) {
            int speed = left + (right - left) / 2;
            int spent = 0;
            for (int j = 0; j < n; j++) {
                spent += (int) Math.ceil((double) piles[j] / speed);
            }
            if (spent <= h) {
                ans = Math.min(ans, speed);
                right = speed - 1;
            } else {
                left = speed + 1;
            }

        }
        return ans;
    }

    public static void main(String[] args) {
        L_875 l = new L_875();
        System.out.println(l.minEatingSpeed(new int[]{3, 6, 7, 11}, 8));
    }
}
