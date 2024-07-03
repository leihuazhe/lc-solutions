package com.shine.data.leetcode;

/**
 * L_190_ReverseBits
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/03 13:38
 */
public class L_190_ReverseBits {

  // you need treat n as an unsigned value
  public int reverseBits(int n) {
    // 1010 ^ 0000 = 01
    return n ^ 1;
  }
}
