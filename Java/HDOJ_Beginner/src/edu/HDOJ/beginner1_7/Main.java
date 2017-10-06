package edu.HDOJ.beginner1_7;
import java.util.Scanner;
public class Main {
	static final int strLength = 10000;
    static int[] result = new int[strLength];  
    static int[] intList = new int[strLength];
	public static void main(String[] args) {
		String ss = null;
		int m = 0;
		//System.out.println("please enter N pairs of M integers with an separator-SPACE:");
		for(Scanner si = new Scanner(System.in);!(ss = si.nextLine()).isEmpty();m++) {
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
			result[m] = sum;
		}
		for (int i = 0; i < m; i++) {
			System.out.println(result[i]);
			if (m-1 != i) {
				System.out.println();
			}
		}		
	}
}