package com.lizhen.test;

public class Wrapper {
    public static void main(String[] args) {
        /**
        Integer i1 = 128;  // 装箱，相当于 Integer.valueOf(128);
        int t = i1; //相当于 i1.intValue() 拆箱
        System.out.println(t);
        */

        /**
        对于–128到127（默认是127）之间的值,被装箱后，会被放在内存里进行重用
        但是如果超出了这个值,系统会重新new 一个对象
        */
        Integer i1 = 200;
        Integer i2 = 200;

        /**
        注意 == 与 equals的区别
        == 它比较的是对象的地址
        equals 比较的是对象的内容
        */
        if(i1==i2) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}
