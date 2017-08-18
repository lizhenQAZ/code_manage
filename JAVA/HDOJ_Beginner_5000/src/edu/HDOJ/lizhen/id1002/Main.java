package edu.HDOJ.lizhen.id1002;
import java.math.BigInteger;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {		
        Scanner sc=new Scanner(System.in);
        while (sc.hasNext()) {
        	int lcn = sc.nextInt();
            for (int i = 1; i <= lcn; i++) {
            	BigInteger la,lb,ans;
            	la = sc.nextBigInteger();
            	lb = sc.nextBigInteger(); 
            	ans = la.add(lb) ;
                System.out.println("Case "+ i +":");
                System.out.println(la + " + " + lb + " = " + ans);
                if(i < lcn) {
                System.out.println();
                }
			}
		}
        sc.close();
	}
}