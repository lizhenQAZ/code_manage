package com.lizhen.test;

public class Condition {
   public static void main(String[] args){
      int a , b;
      a = 10;
      // ��� a ���� 1 ������������ b Ϊ 20������Ϊ 30
      b = (a == 1) ? 20 : 30;
      System.out.println( "Value of b is : " +  b );
 
      // ��� a ���� 10 ������������ b Ϊ 20������Ϊ 30
      b = (a == 10) ? 20 : 30;
      System.out.println( "Value of b is : " + b );
   }
}
