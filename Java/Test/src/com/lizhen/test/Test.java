package com.lizhen.test;

class A1{
    static int i;
    void change(int i1){i=i1;}
}

public class Test{ 
	public void pupAge(){
      int age = 0;
      age = age + 7;
      System.out.println("小狗的年龄是: " + age);
   }
   public static void main(String args[]){
      Test test = new Test();
      test.pupAge();
      A1.i=10;
      A1 a=new A1();
      A1 b=new A1();
      System.out.println(A1.i+","+a.i+","+b.i);//10,10,10
      a.change(40);
      System.out.println(A1.i+","+a.i+","+b.i);//40,40,40
      b.i+=10;
      System.out.println(A1.i+","+a.i+","+b.i);//50,50,50
   }
}
