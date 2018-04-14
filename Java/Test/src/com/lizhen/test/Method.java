package com.lizhen.test;

public class Method {
   /** 主方法 */
   public static void main(String[] args) {
       int i = 5;
       int j = 2;
       int k = max(i, j);
       System.out.println( i + " 和 " + j + " 比较，最大值是：" + k);
       printGrade(78.5);
       int num1 = 1;
       int num2 = 2;
       System.out.println("交换前 num1 的值为：" + num1 + " ，num2 的值为：" + num2);
       // 调用swap方法
       swap(num1, num2);
       System.out.println("交换后 num1 的值为：" + num1 + " ，num2 的值为：" + num2);
       // 获取命令行参数
       for(int p=0; p<args.length; p++){
          System.out.println("args[" + p + "]: " + args[p]);
       }
       // 构造方法
       MyClass t1 = new MyClass();
       MyClass t2 = new MyClass();
       System.out.println(t1.x + " " + t2.x);
       // 调用可变参数的方法
       printMax(34, 3, 3, 2, 56.5);
       printMax(new double[]{1, 2, 3});
   }
   /** 返回两个整数变量较大的值 */
   public static int max(int num1, int num2) {
	   int result;
	   if (num1 > num2)
	      result = num1;
	   else
	      result = num2;
	   return result; 
   }
   // 重载
   public static double max(double num1, double num2) {
	   if (num1 > num2)
	      return num1;
	   else
	      return num2;
   }
   // void返回值
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
   /** 交换两个变量的方法 */
   public static void swap(int n1, int n2) {
     System.out.println("\t\t交换前 n1 的值为：" + n1 + "，n2 的值：" + n2);
     // 交换 n1 与 n2的值
     int temp = n1;
     n1 = n2;
     n2 = temp;
     System.out.println("\t\t交换后 n1 的值为 " + n1 + "，n2 的值：" + n2);
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
    // 以下是构造函数
    MyClass() {
        x = 10;
    }
}
