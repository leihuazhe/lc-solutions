package com.shine.data.shine;

/**
 * TODO
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/06 10:33
 */
public class BitTest {

  public static void main(String[] args) {
    int x = 3;
    boolean b1 = true;
    boolean b2 = false;
    if ((b1 | b2) || (x++ > 4)) {
      System.out.println("x1: " + x++);
    }
    if (!(b1 & b2) && (++x < 4)) {
      System.out.println("x2: " + x);
    }
  }
}
