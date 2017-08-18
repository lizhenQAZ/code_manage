package edu.HDOJ.lizhen.id1013;
import java.math.BigInteger;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		while (sc.hasNext()) {
			BigInteger ia = sc.nextBigInteger();
			String str=ia.toString();
			char[] cha =str.toCharArray();
			long result=0;
			if (ia.equals(BigInteger.valueOf(0))) {
				break;
			}
			for (int i = 0; i < cha.length; i++) {
				result = result+Long.parseLong(Character.toString(cha[i]));
			}
			result = result%10;
			System.out.println(result);
			System.out.println();
		}
		sc.close();
	}
}
