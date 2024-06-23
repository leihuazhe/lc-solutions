package com.shine.data.list.queue.l1700;

import java.util.LinkedHashMap;
import java.util.Map;

public class LRU {

    public static void main(String[] args) {
        Map<String, String> lru = new LinkedHashMap<>(16, 0.75f, true);
        for (int i = 0; i < 10; i++) {
            lru.put(i + "", i + "");
        }
        lru.get("3");
        lru.get("6");
        lru.get("2");
        System.out.println(lru.keySet());
    }
}
