package com.lizhen.test;

public class StringDemo {
   public static void main(String args[]){
      char[] helloArray = { 'r', 'u', 'n', 'o', 'o', 'b'};
      float floatVar = 1.14f;
      int intVar = 12;
      String stringVar = "i am hello!";
      String fs;
      fs = String.format("�����ͱ�����ֵΪ " +
              "%f, ���ͱ�����ֵΪ " +
              " %d, �ַ���������ֵΪ " +
              " %s", floatVar, intVar, stringVar);
      String helloString = new String(helloArray);  
      System.out.println( helloString );
      System.out.println( "���� : " + helloString.length() );
      System.out.println(helloString + " www.baidu.com"); 
      System.out.println("��ʽ���ַ���Ϊ��" + fs); 
   };
}
