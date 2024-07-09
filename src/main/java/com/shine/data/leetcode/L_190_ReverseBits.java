package com.shine.data.leetcode;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.Formatter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * L_190_ReverseBits
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/03 13:38
 */
public class L_190_ReverseBits {

  // you need treat n as an unsigned value
  public int reverseBits(int n,Set<?> x2) {
    Set<?> x = x2;
    System.gc();
    // 1010 ^ 0000 = 01
    return n ^ 1;
  }


  static class Helper {
    private int data = 5;

    public void bump(int inc) {
      inc++;
      data = data + inc;
    }
  }


  public static class Invoice {
    public static String format(String id) {
      return "Invoice" + id;
    }

  }


  public static class SInvoice extends Invoice {

    public SInvoice() {


    }

    public void x() {
    }


    public static String format(String id) {

      return "SInvoice" + id;
    }

  }


  static class X extends Exception {


  }


  static class Parrent {
    static int count = 0;

    public Parrent() {
      count++;
    }
  }


  static class Child extends Parrent {
    public Child() {
      count++;
    }


  }

  interface  AA {
    void me1();
    static void m2() {

    }
  }
  abstract class  BB implements AA {
    abstract void m1();
//     static void m2();
  }

  public static void main(String... args) throws IOException, ParseException {
    Date s = new SimpleDateFormat("yyyy-mm-dd").parse("2021-01-15");
    Calendar c2 = Calendar.getInstance();
    c2.setTime(s);
    System.out.println(c2.get(Calendar.MONTH));

    LocalDate l = LocalDate.parse("2012-01-15", DateTimeFormatter.ofPattern("yyyy-MM-dd"));
    System.out.println(l.getMonthValue());








    List<String> s2 = new ArrayList<>();
    s2.add("1");
    s2.add("2");
    s2.add(0,"3");
    s2.add(1,"4");
    System.out.println(s2);




    StringBuilder builder = new StringBuilder("C");
    Formatter formmater = new Formatter(builder);
    formmater.format("%s%s", "A", "B");
    System.out.println(formmater);
    formmater.format("%-2s", "B");
    System.out.println(formmater);
    formmater.format("%b", null);
    System.out.println(formmater);







    System.out.println(Parrent.count);
    Child c = new Child();
    System.out.println(Parrent.count);


    List<Map<List<String>, List<String>>> list = new ArrayList<>();
    list.add(new HashMap<>());
    list.forEach(e -> System.out.println(e));
    Set<String> set = new LinkedHashSet<>();
    set.add("1");
    set.add("3");
    set.add("3");
    set.add("2");
    set.add("3");
    set.add("1");
//    set.forEach(s -> System.out.print(s + "-"));



    int a = 9, b = 2;
    float f;
    f = a / b;
    System.out.println(f);
    f = f / 2;
    System.out.println(f);



//    byte c1[] = {10, 20, 30, 40, 50};
//    byte c2[] = {60, 70, 80, 90};
//    ByteArrayOutputStream b1 = new ByteArrayOutputStream();
//    ByteArrayOutputStream b2 = new ByteArrayOutputStream(10);
//    b2.write(100);
//    System.out.println(b2.size());
//    b2.write(c1, 0, c2.length);
//    System.out.println(b2.size());
//    b2.reset();
//    b1.writeTo(b2);
//    System.out.println(b1.size());



//    Helper h = new Helper();
//    int data = 2;
//    h.bump(data);
//    System.out.println(h.data);
//    System.out.println(data);
//
////    ResourceBundle.getBundle("Message",new Locale("zh","CN"));
//
//    System.out.println(LocalDate.of(2015,4,4).format(DateTimeFormatter.ofPattern("E, MMM dd, yyyy")));
//    System.out.println(LocalDate.of(2015,4,4).format(DateTimeFormatter.ofPattern("MM/dd/yy")));
//
//
//
//
//
//    System.out.println(Stream.of("green","yellow","blue")
//        .max((s1,s2) -> s1.compareTo(s2))
//        .filter(s -> s.endsWith("n"))
//        .orElse("yellow")
//
//    )
//
//    ;



//    Invoice s = new SInvoice();
//    System.out.println(s.format("1"));



//    Integer num1 = new Integer(1);
//    Integer num2 = num1;
//    num1 += 1;
//    System.out.println(num1);
//    System.out.println(num2);

  }
}
