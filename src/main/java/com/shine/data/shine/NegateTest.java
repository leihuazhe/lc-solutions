package com.shine.data.shine;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TimeZone;
import java.util.function.Predicate;

/**
 * TODO
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/06 10:21
 */
public class NegateTest {

  public static void main(String[] args) {
    TimeZone.getTimeZone("GMT");



    //collection 的踩坑
    List<String> letters = new ArrayList<>(Arrays.asList("D", "B", "A", "C", "F", "G"));
    Predicate<String> p1 = s -> s.compareTo("C") > 0;
    Predicate<String> p2 = s -> s.equals("B");
    letters.removeIf(p1.negate().or(p2));
    letters.sort((s1, s2) -> s1.compareTo(s2));
    System.out.println(letters);

  }
}
