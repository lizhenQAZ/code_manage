package edu.HDOJ.beginner1_3;
import java.util.*;
public class Main {
	public static void main(String[] args) {
		int[] result = new int[10000];  
		int j = 0;
		String ss = null;
		System.out.println("please enter two pairs of two integers with an separator-SPACE:");
		for(Scanner si = new Scanner(System.in);;) {
			ss = si.nextLine();
		    String[] match = ss.split("\\s*", 2);
		    if (0 == Integer.parseInt(match[0]) && 0 == Integer.parseInt(match[1])) {
		    	break;
			}
		    result[j] = Integer.parseInt(match[0])+Integer.parseInt(match[1]);
		    j++;
		}
		for (int i = 0; i < result.length; i++) {
			if (result[i] != 0) {
			System.out.println(result[i]);
			}
		}		
	}
}