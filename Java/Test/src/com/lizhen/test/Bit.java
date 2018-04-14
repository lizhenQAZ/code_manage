package com.lizhen.test;

public class Bit {
	public static void main(String[] args) {
		Byte a = 0x3c;
		Byte b = 0x0d;
		System.out.println(a);
		System.out.println(b);
		System.out.println(a&b);
		System.out.println(a|b);
		System.out.println(a^b);
		System.out.println(~a);
		System.out.println("a << 2  = " + (a<<2) );
		System.out.println("a >> 2  = " + (a>>2) );
	    System.out.println("a >>> 2 = " + (a>>>2));
	}
}
