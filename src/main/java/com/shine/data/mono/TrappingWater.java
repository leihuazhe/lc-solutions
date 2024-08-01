package com.shine.data.mono;

import java.util.ArrayList;
import java.util.List;

/**
 * time: O(N)
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/31 17:59
 */
public class TrappingWater {
  public int trap(int[] height) {
    int ans = 0;
    if (height == null || height.length == 0) {
      return ans;
    }
    List<Integer> st = new ArrayList<>();
    for (int i = 0; i < height.length; i++) {
      int h = height[i];
      while (!st.isEmpty() && h >= height[st.getLast()]) {
        int middle = st.removeLast();
        if (st.isEmpty()) {
          break;
        }
        int left = st.getLast();
        int dh = Math.min(h, height[left]) - height[middle];
        int distance = i - left - 1;
        ans += dh * distance;
      }
      st.add(i);
    }
    return ans;

  }

  public static void main(String[] args) {
    TrappingWater solutions = new TrappingWater();
    int ans = solutions.trap(new int[] {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1});
    System.out.println(ans);
  }
}
