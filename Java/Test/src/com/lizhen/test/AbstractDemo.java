/* �ļ��� : AbstractDemo.java */
package com.lizhen.test;

public class AbstractDemo
{
   public static void main(String [] args)
   {
      /* �����ǲ�����ģ����������� */
      Employee3 e = new Employee3("George W.", "Houston, TX", 43);
 
      System.out.println("\n Call mailCheck using Employee reference--");
      e.mailCheck();
    }
}
