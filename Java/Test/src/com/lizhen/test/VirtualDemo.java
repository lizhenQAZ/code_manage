/* �ļ��� : VirtualDemo.java */
package com.lizhen.test;

public class VirtualDemo {
   public static void main(String [] args) {
      Salary s = new Salary("Ա�� A", "����", 3, 3600.00);
      Employee2 e = new Salary("Ա�� B", "�Ϻ�", 2, 2400.00);
      System.out.println("ʹ�� Salary �����õ��� mailCheck -- ");
      s.mailCheck();
      System.out.println("\nʹ�� Employee �����õ��� mailCheck--");
      e.mailCheck();
    }
}
