package com.lizhen.test;

public class TestOverloading {
    private static int i = 1;
    private static double l = 3.1415;
    private static String k = "��������";
	
    public int test(){
        System.out.println("test1");
        return 1;
    }
 
    public void test(int a){
        System.out.println("test2");
    } 
    
    public void test(double a){
        System.out.println("�������˸�����:"+a);
    }   
 
    public void test(String a){
        System.out.println("���������ַ���:"+a);
    }
    
    //����������������˳��ͬ
    public String test(int a, String s){
        System.out.println("test3");
        return "returntest3";
    }   
 
    public String test(String s, int a){
        System.out.println("test4");
        return "returntest4";
    }   
 
    public static void main(String[] args){
    	TestOverloading o = new TestOverloading();
        System.out.println(o.test());
        o.test(1);
        System.out.println(o.test(1,"test3"));
        System.out.println(o.test("test4",1));
        o.test(i);
        o.test(l);
        o.test(k);
    }
}
