package com.lizhen.test;

class FreshJuice {
	   enum FreshJuiceSize{ SMALL, MEDIUM , LARGE }
	   FreshJuiceSize size;
	}
	 
public class TestFreshJuice {
   public static void main(String []args){
      FreshJuice juice = new FreshJuice();
      juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
      System.out.println(juice.size);
   }
}
