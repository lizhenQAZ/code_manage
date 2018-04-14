package com.lizhen.test;

public class Method {
   /** ������ */
   public static void main(String[] args) {
       int i = 5;
       int j = 2;
       int k = max(i, j);
       System.out.println( i + " �� " + j + " �Ƚϣ����ֵ�ǣ�" + k);
       printGrade(78.5);
       int num1 = 1;
       int num2 = 2;
       System.out.println("����ǰ num1 ��ֵΪ��" + num1 + " ��num2 ��ֵΪ��" + num2);
       // ����swap����
       swap(num1, num2);
       System.out.println("������ num1 ��ֵΪ��" + num1 + " ��num2 ��ֵΪ��" + num2);
       // ��ȡ�����в���
       for(int p=0; p<args.length; p++){
          System.out.println("args[" + p + "]: " + args[p]);
       }
       // ���췽��
       MyClass t1 = new MyClass();
       MyClass t2 = new MyClass();
       System.out.println(t1.x + " " + t2.x);
       // ���ÿɱ�����ķ���
       printMax(34, 3, 3, 2, 56.5);
       printMax(new double[]{1, 2, 3});
   }
   /** �����������������ϴ��ֵ */
   public static int max(int num1, int num2) {
	   int result;
	   if (num1 > num2)
	      result = num1;
	   else
	      result = num2;
	   return result; 
   }
   // ����
   public static double max(double num1, double num2) {
	   if (num1 > num2)
	      return num1;
	   else
	      return num2;
   }
   // void����ֵ
   public static void printGrade(double score) {
	   if (score >= 90.0) {
	      System.out.println('A');
	   }
	   else if (score >= 80.0) {
	      System.out.println('B');
	   }
	   else if (score >= 70.0) {
	      System.out.println('C');
	   }
	   else if (score >= 60.0) {
	      System.out.println('D');
	   }
	   else {
		  System.out.println('F');
	   }
   }
   /** �������������ķ��� */
   public static void swap(int n1, int n2) {
     System.out.println("\t\t����ǰ n1 ��ֵΪ��" + n1 + "��n2 ��ֵ��" + n2);
     // ���� n1 �� n2��ֵ
     int temp = n1;
     n1 = n2;
     n2 = temp;
     System.out.println("\t\t������ n1 ��ֵΪ " + n1 + "��n2 ��ֵ��" + n2);
   }
   public static void printMax( double... numbers) {
       if (numbers.length == 0) {
           System.out.println("No argument passed");
           return;
       }
       double result = numbers[0];
       for (int i = 1; i <  numbers.length; i++){
           if (numbers[i] >  result) {
               result = numbers[i];
           }
       }
       System.out.println("The max value is " + result);
   }
}

class MyClass {
    int x;
    // �����ǹ��캯��
    MyClass() {
        x = 10;
    }
}
