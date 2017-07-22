package edu.HDOJ.beginner1_8;
import java.util.Scanner;
public class Main {
	static final int strLength = 10000;
    static int[] result = new int[strLength];  
    static int[] intList = new int[strLength];
	public static void main(String[] args) {
		String ss = null;
		//System.out.println("please enter N pairs of integers:");
		Scanner si = new Scanner(System.in);
		int intLine = Integer.parseInt(si.nextLine());
		//System.out.println("please enter N pairs of M integers with an separator-SPACE:");
		for(int k = 0;k < intLine;k++) {
			Scanner si2 = new Scanner(System.in);
			ss = si2.nextLine();
		    String[] match = ss.split("\\s",100);		    
			int sum = Integer.parseInt(match[0]);
			for (int i = 1; i < match.length; i++) {
				for (int j = 0; j < i; j++) {
					if (match[i].equals(match[j])) {
						intList[i] = 0;
						break;
					}
					else {
						intList[i] = Integer.parseInt(match[i]);
					}
					
				}
				sum += intList[i];
			}			
			result[k] = sum;
			if (intLine-1 == k)
			{
				si2.close();
			}
		}
		si.close();
		for (int i = 0; i < intLine; i++) {
			System.out.println(result[i]);
			if (intLine-1 != i) {
				System.out.println();
			}
		}		
	}
}