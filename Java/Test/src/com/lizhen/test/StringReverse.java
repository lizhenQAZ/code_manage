package com.lizhen.test;

public class StringReverse {
    public static void main(String args[]) {
        String str = "helloworld";
        char[] data = str.toCharArray();// 将字符串转为数组
        for (int x = 0; x < data.length; x++) {
            System.out.print(data[x] + "  ");
            data[x] -= 32;
            System.out.print(data[x] + "  ");
        }
        System.out.println(new String(data));
    }
}
