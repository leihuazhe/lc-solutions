package com.shine.data.leetcode;

import java.util.ArrayList;
import java.util.List;

public class L_54 {

    enum Direction {
        RIGHT, DOWN, LEFT, UP
    }


    public List<Integer> spiralOrder(int[][] matrix) {
        // line length
        int m = matrix[0].length;
        // col length
        int n = matrix.length;
        //
        List<Integer> ans = new ArrayList<>();
        int i = 0, j = 0;
        Direction direction = Direction.RIGHT;
        // iterate through the whole matrix.
        int round = 0;
        while (ans.size() < m * n) {
            switch (direction) {
                case RIGHT:
                    while (j < m - round) {
                        ans.add(matrix[i][j]);
                        j++;
                    }
                    j--;
                    i++;
                    direction = Direction.DOWN;
                    break;
                case DOWN:
                    while (i < n - round) {
                        ans.add(matrix[i][j]);
                        i++;
                    }
                    i--;
                    j--;
                    direction = Direction.LEFT;
                    break;
                case LEFT:
                    while (j >= round) {
                        ans.add(matrix[i][j]);
                        j--;
                    }
                    j++;
                    i++;
                    direction = Direction.UP;
                    break;
                case UP:
                    while (i >= round) {
                        ans.add(matrix[i][j]);
                        i--;
                    }
                    i++;
                    j++;
                    direction = Direction.LEFT;
                    round++;
                    break;
            }

        }
        return ans;


    }

    public static void main(String[] args) {
        int[][] matrix = new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        L_54 l = new L_54();
        System.out.println(l.spiralOrder(matrix));
    }
}
