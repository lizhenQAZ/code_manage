package com.lizhen.test;
import java.io.Console;
import java.util.Scanner; 

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // �Ӽ��̽�������
        // next��ʽ�����ַ���
        System.out.println("next��ʽ���գ�");
        // �ж��Ƿ�������
        if (scan.hasNext()) {
            String str1 = scan.next();
            System.out.println("���������Ϊ��" + str1);
        }
        
        Scanner scan2 = new Scanner(System.in);
        // nextLine��ʽ�����ַ���
        System.out.println("nextLine��ʽ���գ�");
        // �ж��Ƿ�������
        if (scan2.hasNextLine()) {
            String str2 = scan2.nextLine();
            System.out.println("���������Ϊ��" + str2);
        }
        
        Scanner scan3 = new Scanner(System.in);
        // �Ӽ��̽�������
        int i = 0;
        float f = 0.0f;
        System.out.print("����������");
        if (scan3.hasNextInt()) {
            // �ж�������Ƿ�������
            i = scan3.nextInt();
            // ��������
            System.out.println("�������ݣ�" + i);
        } else {
            // ����������Ϣ
            System.out.println("����Ĳ���������");
        }
        System.out.print("����С����");
        if (scan3.hasNextFloat()) {
            // �ж�������Ƿ���С��
            f = scan3.nextFloat();
            // ����С��
            System.out.println("С�����ݣ�" + f);
        } else {
            // ����������Ϣ
            System.out.println("����Ĳ���С����");
        }
        
        Scanner scan4 = new Scanner(System.in);
        double sum = 0;
        int m = 0;
        while (scan4.hasNextDouble()) {
            double x = scan4.nextDouble();
            m = m + 1;
            sum = sum + x;
        }
        System.out.println(m + "�����ĺ�Ϊ" + sum);
        System.out.println(m + "������ƽ��ֵ��" + (sum / m));
        
        // ��ȡ�û���������
        Console cons = System.console();
        String username = cons.readLine("User name: ");
        char[] passwd = cons.readPassword("Password: ");
        
        scan.close();
        scan2.close();
        scan3.close();
        scan4.close();
    }
}
