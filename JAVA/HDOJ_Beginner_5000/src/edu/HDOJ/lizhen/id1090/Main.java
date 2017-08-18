package edu.HDOJ.lizhen.id1090;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			int max = sc.nextInt();
			for (int i = 0; i < max; i++) {
				int ia = sc.nextInt();
				int ib = sc.nextInt();	
				int sum = ia + ib;
				System.out.println(sum);
			}
			
		}
		sc.close();
	}

}
