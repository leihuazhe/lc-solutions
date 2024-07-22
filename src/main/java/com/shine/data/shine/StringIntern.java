package com.shine.data.shine;

/**
 * StringIntern
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/19 10:33
 */
public class StringIntern {

  public static void main(String[] args) {
    String s1 = "abc";
    String s2 = new String("abc");

    System.out.println(System.identityHashCode(s1));
    System.out.println(System.identityHashCode(s2));
    System.out.println(System.identityHashCode(s2.intern()));
  }
}
