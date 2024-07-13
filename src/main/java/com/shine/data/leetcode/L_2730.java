package com.shine.data.leetcode;

public class L_2730 {
    public int longestSemiRepetitiveSubstring(String s) {
        int repeatCnt = 0, res = 1;
        for (int j = 1, i = 0; j < s.length(); j++) {
            if (s.charAt(j) == s.charAt(j - 1)) repeatCnt++;
            if (repeatCnt > 1) {
                if (s.charAt(i) == s.charAt(i + 1)) {
                    repeatCnt--;
                }
                i++;
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }

    public static void main(String[] args) {
        L_2730 s = new L_2730();
        System.out.println(s.longestSemiRepetitiveSubstring("1632334567998"));
        /*
            l         r
            1632334567998
             l         r
            1632334567998
              l         r
            1632334567998




         */


        //System.out.println(s.longestSemiRepetitiveSubstring("1111111"));
    }
}
