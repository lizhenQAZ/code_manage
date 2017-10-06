package edu.HDOJ.lizhen.id1106;
import java.util.*;
public class Main {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()) {
			String str = sc.next();
			String[] strList = str.split("5+"); 
			List <Integer> iList = new ArrayList<Integer>();
			for (int i = 0; i < strList.length; i++) {
				if (!strList[i].isEmpty()){
					int count = 0;
					for (int j = 0; j < strList[i].length(); j++) {
						if(strList[i].charAt(j) == '0') {
							count++;
						}
						else {
							break;
						}
					}
					if (count == strList[i].length()) {
						iList.add(0);
						continue;
					}
					else {
						iList.add(Integer.parseInt(String.copyValueOf(strList[i].toCharArray(), count, (strList[i].length()-count))));
						continue;
					}
				}
			}			
			Collections.sort(iList);
			for (int i = 0; i < strList.length; i++) {
				System.out.print(iList.toArray()[i]);
				if (i != (strList.length-1)) {
					System.out.print(" ");
				}
			}
			System.out.println();
		}
		sc.close();
	}
}