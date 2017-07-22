package edu.HDOJ.lizhen.id1001;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        while (sc.hasNextLong()) {
            long max = sc.nextLong();
            long sum = 0;
            for (long i = 0; i <= max; i++) {
            	sum += i;			
			}
            System.out.println(sum);
            System.out.println();
		}
        sc.close();
	}
}