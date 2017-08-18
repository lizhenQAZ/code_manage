package edu.HDOJ.lizhen.id1091;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			int ia = sc.nextInt();
			int ib = sc.nextInt();
			if (0==ia && 0==ib)
			{
				break;
			}
			int sum = ia + ib;
			System.out.println(sum);
		}
		sc.close();
	}

}
