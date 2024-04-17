package com.shine.data.list.queue.l1700;

// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
public class Version2 {

    public int countStudents(int[] students, int[] sandwiches) {

        // students order suitable for the queue D.S.
        // This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
        // using loop and define the break conditions.
        Queue queue = new Queue();
        for (int s : students) {
            queue.enqueue(s);
        }
        int sandIndex = 0;
        int res = 0;
        int seq = 0;
        while (seq != queue.size()) {
            int student = queue.dequeue();
            if (student == sandwiches[sandIndex]) {
                sandIndex++;
                seq = 0;
            } else {
                queue.enqueue(student);
                seq++;
            }
        }

        return queue.size();
    }

    public static class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
        }
    }

    public static class Queue {
        //front
        ListNode left;
        //back
        ListNode right;
        int size;


        void enqueue(int val) {
            ListNode node = new ListNode(val);
            if (right == null) {
                left = node;
                right = node;
            } else {
                right.next = node;
                right = right.next;
            }
            size++;
        }

        int dequeue() {
            if (left == null) {
                return -1;
            }
            size--;
            int val = left.val;
            left = left.next;
            return val;
        }

        int size() {
            return size;
        }
    }
}
