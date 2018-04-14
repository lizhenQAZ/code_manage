/* ÎÄ¼þÃû : AbstractDemo2.java */
package com.lizhen.test;

public class AbstractDemo2
{
   public static void main(String [] args)
   {
      Salary2 s = new Salary2("Mohd Mohtashim", "Ambehta, UP", 3, 3600.00);
      Employee3 e = new Salary2("John Adams", "Boston, MA", 2, 2400.00);
 
      System.out.println("Call mailCheck using Salary reference --");
      s.mailCheck();
 
      System.out.println("\n Call mailCheck using Employee reference--");
      e.mailCheck();
    }
}