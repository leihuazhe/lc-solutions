package com.shine.data.shine;

public class SortList {

    public static void main(String[] args) {
        int[] array1 = {5444567, 332, 123, 456};
        int[] array2 = {5444566, 312, 223, 356};
        int maxLen = 0;
        for (int num1 : array1) {
            String num1Str = String.valueOf(num1);
            for (int num2 : array2) {
                int commonLen = 0;
                String prefix = num1Str.substring(0, commonLen + 1);
                String str = String.valueOf(num2);
                while (str.startsWith(prefix)) {
                    commonLen++;
                    prefix = num1Str.substring(0, commonLen + 1);
                }
                maxLen = Math.max(maxLen, commonLen);
            }

        }
        System.out.println(maxLen);

    }

}
