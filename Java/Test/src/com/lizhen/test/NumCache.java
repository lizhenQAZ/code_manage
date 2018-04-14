package com.lizhen.test;

public class NumCache {
	public static void main(String[] args) {
		Integer a = 10;
		Integer b = 10;
		System.out.println(a == b);        // true
		System.out.println(a.equals(b));   // true
		Integer c = 1000;
		Integer d = 1000;
		System.out.println(c == d);        // false
		System.out.println(c.equals(d));   // true
	}
}
