package edu.HDOJ.lizhen.id1108;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			int ia = sc.nextInt();
			int ib = sc.nextInt();
			int min = ia<ib?ia:ib;
			int max = ia>ib?ia:ib;
			int maxComDiv = 1;
		    int minComMul = 1;
		    if (max % min == 0) {
				System.out.println(max);
			}
		    else {
			    for (int i=1;i<min;i++) {
					if(0 == (min%i) && 0 == (max%i)) {
						maxComDiv = i;
					}
				}
			    minComMul = (ia*ib)/maxComDiv;
			    System.out.println(minComMul);
			}
		}
		sc.close();
	}
}
