package com.lizhen.test;
//import java.io.*;

public class TestEmployee{
   public static void main(String args[]){
      /* ʹ�ù����������������� */
      Employee empOne = new Employee("test1");
      Employee empTwo = new Employee("test2");
 
      // ��������������ĳ�Ա����
      empOne.empAge(26);
      empOne.empDesignation("�߼�����Ա");
      empOne.empSalary(1000);
      empOne.printEmployee();
 
      empTwo.empAge(21);
      empTwo.empDesignation("�������Ա");
      empTwo.empSalary(500);
      empTwo.printEmployee();
   }
}