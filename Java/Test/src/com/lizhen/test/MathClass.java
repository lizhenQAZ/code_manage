package com.lizhen.test;

public class MathClass {
	public static void main (String []args) {  
	    double[] nums = { 1.4, 1.5, 1.6, -1.4, -1.5, -1.6 };
	    System.out.println("90 �ȵ�����ֵ��" + Math.sin(Math.PI/2));  
	    System.out.println("0�ȵ�����ֵ��" + Math.cos(0));  
	    System.out.println("60�ȵ�����ֵ��" + Math.tan(Math.PI/3));  
	    System.out.println("1�ķ�����ֵ�� " + Math.atan(1));  
	    System.out.println("��/2�ĽǶ�ֵ��" + Math.toDegrees(Math.PI/2));  
	    System.out.println(Math.PI);  
	    for (double num : nums) {   
	    	test(num);   
		}  
	}
	
    private static void test(double num) {
    	System.out.println("Num(" + num + ")=" + num);  
	    System.out.println("Math.floor(" + num + ")=" + Math.floor(num));   
	    System.out.println("Math.round(" + num + ")=" + Math.round(num));   
	    System.out.println("Math.ceil(" + num + ")=" + Math.ceil(num));   
	}  
}
