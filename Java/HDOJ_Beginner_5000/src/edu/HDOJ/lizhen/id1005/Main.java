package edu.HDOJ.lizhen.id1005;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int n = sc.nextInt();
			if (0==a && 0==b && 0==n) {
				sc.close();
				break;
			}
			int result = add(a, b, n);
			System.out.println(result);
		}		
	}
	
	public static int add(int a,int b ,int n) {
		if (n==1||n==2) {
			return 1;
		}
		else {
			int sum = (a*add(a,b,n-1)+b*add(a,b,n-2))%7;
			return sum;
		}
	}

}
