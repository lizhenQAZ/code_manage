package com.lizhen.test;
import java.util.Scanner;
import java.util.StringTokenizer;

public class StringTokenFormat {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.println("�������ݣ�");
        StringTokenizer stringTokenizer=new StringTokenizer(scanner.nextLine());
        System.out.println("�ָ���");
        while(stringTokenizer.hasMoreTokens()){
            System.out.println(stringTokenizer.nextToken());
        }
    }
}
