package com.shine.data.heap;

import java.util.PriorityQueue;

/**
 * HeapTest
 *
 * @author leihz
 * @version 1.0.0
 * @since 2024/07/01 17:05
 */
public class HeapTest {

  public static void main(String[] args) {
    PriorityQueue<Integer> queue = new PriorityQueue<>();

    queue.offer(1);
    queue.offer(2);
    queue.offer(10);
    queue.offer(7);

    while (!queue.isEmpty()){
      System.out.println(queue.poll());
    }



  }
}
