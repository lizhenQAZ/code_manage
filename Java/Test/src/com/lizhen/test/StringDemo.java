package com.lizhen.test;

public class StringDemo {
   public static void main(String args[]){
      char[] helloArray = { 'r', 'u', 'n', 'o', 'o', 'b'};
      float floatVar = 1.14f;
      int intVar = 12;
      String stringVar = "i am hello!";
      String fs;
      fs = String.format("浮点型变量的值为 " +
              "%f, 整型变量的值为 " +
              " %d, 字符串变量的值为 " +
              " %s", floatVar, intVar, stringVar);
      String helloString = new String(helloArray);  
      System.out.println( helloString );
      System.out.println( "长度 : " + helloString.length() );
      System.out.println(helloString + " www.baidu.com"); 
      System.out.println("格式化字符串为：" + fs); 
   };
}
