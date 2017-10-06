package edu.HDOJ.beginner1_4;
import java.util.Scanner;
public class Main {
	static final int strLength = 10000;
    static int[] result = new int[strLength];  
    static int[] intList = new int[strLength];
	public static void main(String[] args) {
		int m = 0;
		String ss = null;
		System.out.println("please enter two pairs of two integers with an separator-SPACE:");
		for(Scanner si = new Scanner(System.in);;) {
			ss = si.nextLine();
		    String[] match = ss.split("\\s",100);
		    if (0 == Integer.parseInt(match[0])) {
		    	si.close();
		    	break;
			}
		    
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
		    m++;
		}
		for (int i = 0; i < m; i++) {
			System.out.println(result[i]);
		}		
	}
}