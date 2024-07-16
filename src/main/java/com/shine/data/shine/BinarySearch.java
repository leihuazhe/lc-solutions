package com.shine.data.shine;

/**
 * BinarySearch
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/15 18:30
 */
public class BinarySearch {


  public static void main(String[] args) {
    System.currentTimeMillis();
    System.out.println(leftBound(new int[] {1, 2, 3, 4, 4, 4, 6, 6, 7}, 5));
    System.out.println(lowerBound(new int[] {1, 2, 3, 4, 4, 4, 5, 6, 7}, 4));
    System.out.println(upperBound(new int[] {1, 2, 3, 4, 4, 4, 5, 6, 7}, 4));
    //
    System.out.println(rightBound(new int[] {1, 2, 3, 4, 4, 4, 6, 6, 7}, 5));
    System.out.println(rightBoundGreate(new int[] {1, 2, 3, 4, 4, 4, 6, 6, 7}, 5));
  }


  // 闭区间写法 low bound, 第一个 小于等于 target 的值.
  private static int lowerBound(int[] nums, int target) {
    int[] x = {1,2};
    int left = 0, right = nums.length - 1; // 闭区间 [left, right]
    while (left <= right) { // 区间不为空
      // 循环不变量：
      // nums[left-1] < target
      // nums[right+1] >= target
      int mid = left + (right - left) / 2;
      if (nums[mid] < target) {
        left = mid + 1; // 范围缩小到 [mid+1, right]
      } else {
        right = mid - 1; // 范围缩小到 [left, mid-1]
      }
    }
    return left;
  }

  private static int upperBound(int[] nums, int target) {
    int left = 0, right = nums.length - 1; // 闭区间 [left, right]
    while (left <= right) { // 区间不为空
      // 循环不变量：
      // nums[left-1] < target
      // nums[right+1] >= target
      int mid = left + (right - left) / 2;
      if (nums[mid] <= target) {
        left = mid + 1; // 范围缩小到 [mid+1, right]
      } else {
        right = mid - 1; // 范围缩小到 [left, mid-1]
      }
    }
    return left;
  }



  public static int leftBound(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
      int mid = l + (r - l) / 2;
      if (nums[mid] < target) { // red
        l = mid + 1;
      } else { // blue
        r = mid - 1;
      }
    }
    return r;
  }

  public static int leftBound2(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
      int mid = l + (r - l) / 2;
      if (nums[mid] < target) { // red
        l = mid + 1;
      } else { // blue
        r = mid - 1;
      }
    }
    return r;
  }

  public static int rightBound(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
      int mid = l + (r - l) / 2;
      if (nums[mid] <= target) { // red
        l = mid + 1;
      } else { // blue
        r = mid - 1;
      }
    }
    return r;
  }

  public static int rightBoundGreate(int[] nums, int target) { // n >= target
    int l = 0, r = nums.length - 1;
    while (l <= r) {
      int mid = l + (r - l) / 2;
      if (nums[mid] < target) { // red
        l = mid + 1;
      } else { // blue
        r = mid - 1;
      }
    }
    return l;
  }
}
