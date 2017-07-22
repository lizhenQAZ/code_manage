package edu.HDOJ.lizhen.id1042;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextInt())
		{
			int n = sc.nextInt();
			System.out.println(multiply(n));
		}
		sc.close();
	}
	public static int multiply(int n) {
		if (1 == n)
			return 1;
		else{ 
			int value = n*multiply((n-1));
			return value;
		}
	}
}
