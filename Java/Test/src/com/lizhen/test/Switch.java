package com.lizhen.test;

public class Switch {
   public static void main(String args[]){
      //char grade = args[0].charAt(0);
      char grade = 'C';
      switch(grade)
      {
         case 'A' :
            System.out.println("����"); 
            break;
         case 'B' :
         case 'C' :
            System.out.println("����");
            break;
         case 'D' :
            System.out.println("����");
         case 'F' :
            System.out.println("����Ҫ��Ŭ��Ŭ��");
            break;
         default :
            System.out.println("δ֪�ȼ�");
      }
      System.out.println("��ĵȼ��� " + grade);
   }
}
