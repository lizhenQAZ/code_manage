package com.lizhen.test;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Fileio {
    public static void main(String[] args) throws FileNotFoundException {
        int[] arr=new int[10];
        int i=0;
        Scanner sc=new Scanner(new File("com\\lizhen\\test\\Fileio.txt"));
        while(sc.hasNextInt()) {
            arr[i]=sc.nextInt();
            i++;
        }
        sc.close();
        System.out.printf("��ȡ�� %d ����\r\n",i);
        for(int j=0;j<i;j++) {
            System.out.println(arr[j]);
        }
    }
}
