package edu.HDOJ.lizhen.id1021;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		while (sc.hasNext()) {
			long la = sc.nextLong();
			long result =add(la);
			if (result % 3 != 0) {
				System.out.println("no");
			}
			else {
				System.out.println("yes");
			}
		}
		sc.close();
	}
	public static long add(Long num) {
		if (0 == num) {
			return 7;
		}
		else if (1 == num) {
			return 11;
		}
		else {
			long sum =add(num-1)+add(num-2);
			return sum;
		}
	}
}
