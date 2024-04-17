package com.shine.data.list.queue;


/**
 * SUGGESTED PROBLEMS
 * <p>
 * https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
 * <p>
 * https://leetcode.com/problems/implement-stack-using-queues/
 */
public class Queue {
    // f x x x x x x b
    ListNode left;  // front of Queue   front -> [1,2,3]
    ListNode right; // back of Queue   [1,2,3] <- back

    public Queue() {
        this.left = null;
        this.right = null;
    }

    public void enqueue(int val) {
        ListNode newNode = new ListNode(val);
        if (this.right != null) {
            // Queue is not empty
            this.right.next = newNode;
            this.right = this.right.next;
        } else {
            // Queue is empty
            this.left = newNode;
            this.right = newNode;
        }
    }

    public int dequeue() {
        if (this.left == null) {
            // Queue is empty
            System.exit(0);
        }
        int val = this.left.val;
        this.left = this.left.next;
        return val;

    }

    public void print() {
        ListNode cur = this.left;
        while (cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println();
    }

    public static class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
        }
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        for (int i = 0; i < 10; i++) {
            queue.enqueue(i);
        }
        queue.print();
        System.out.println("dequeue: " + queue.dequeue());
        System.out.println("dequeue: " + queue.dequeue());
        queue.print();
    }

}