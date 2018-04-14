package com.lizhen.test;

public class TestStatic {
    private static int staticInt = 2;
    private int random = 2;

    public TestStatic() {
        staticInt++;
        random++;
        System.out.println("staticInt = "+staticInt+"  random = "+random);
    }

    public static void main(String[] args) {
    	 System.out.println("���������������ֵ�仯");
    	 TestStatic test = new TestStatic();
         System.out.println("  ʵ��1��staticInt:" + test.staticInt + "----random:" + test.random);
         TestStatic test2 = new TestStatic();
         System.out.println("  ʵ��2��staticInt:" + test.staticInt + "----random:" + test.random);
         System.out.println("��̬������ֵ");
         System.out.println("  ��̬����������:" + A.staticA);
         A a = new A();
         System.out.println("  ������������:" + a.staticA);
         a.toChange();
         System.out.println("  ��̬����1������:" + A.staticA);
         a.toChange2();
         System.out.println("  ��̬����2������:" + A.staticA);
         System.out.println("������ֵ");
         System.out.println("  ��̬��丳ֵ:" + B.staticB);
    }
}

class A { 
    public static  String  staticA ="A" ;  
    //��̬�����޸�ֵ 
    static{  staticA ="A1"; } 
    //�������޸�ֵ
    public A (){  staticA ="A2"; } 
    //��̬���������� 
    public static void toChange(){  staticA ="A3"; } 
    public static void toChange2(){  staticA ="A4"; }  
}

class B { 
    public static final String  staticB ;  // �����븳ֵ���� 
    static{  staticB ="B"; }
}
