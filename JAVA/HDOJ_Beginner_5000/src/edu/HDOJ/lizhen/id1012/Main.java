package edu.HDOJ.lizhen.id1012;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		while (sc.hasNext()) {
			int n = sc.nextInt();
			double sum = 2;
			if (0 == n) {
				System.out.println(1);
			}
			if (1 == n) {
				System.out.println(2);
			}
			else {
				for (int i = 2; i <= n; i++) {
					sum =sum + 1.0/multiply(i);
				}
				System.out.println(sum);
			}
		}
		sc.close();
	}
	public static int multiply(int n) {
		int result=1;
		for (int i = 2; i <= n; i++) {
			result=result*i;
		}
		return result;
	}
}
