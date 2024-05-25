package com.shine.data.shine;

import java.util.Arrays;
import java.util.stream.Collectors;

public class EncodeDecode {


    public static void main(String[] args) {
        String s = "";
        Arrays.stream(s.split(",")).collect(Collectors.toList());
    }
}
