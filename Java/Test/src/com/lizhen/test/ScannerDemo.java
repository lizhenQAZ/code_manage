package com.lizhen.test;
import java.io.Console;
import java.util.Scanner; 

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // 从键盘接收数据
        // next方式接收字符串
        System.out.println("next方式接收：");
        // 判断是否还有输入
        if (scan.hasNext()) {
            String str1 = scan.next();
            System.out.println("输入的数据为：" + str1);
        }
        
        Scanner scan2 = new Scanner(System.in);
        // nextLine方式接收字符串
        System.out.println("nextLine方式接收：");
        // 判断是否还有输入
        if (scan2.hasNextLine()) {
            String str2 = scan2.nextLine();
            System.out.println("输入的数据为：" + str2);
        }
        
        Scanner scan3 = new Scanner(System.in);
        // 从键盘接收数据
        int i = 0;
        float f = 0.0f;
        System.out.print("输入整数：");
        if (scan3.hasNextInt()) {
            // 判断输入的是否是整数
            i = scan3.nextInt();
            // 接收整数
            System.out.println("整数数据：" + i);
        } else {
            // 输入错误的信息
            System.out.println("输入的不是整数！");
        }
        System.out.print("输入小数：");
        if (scan3.hasNextFloat()) {
            // 判断输入的是否是小数
            f = scan3.nextFloat();
            // 接收小数
            System.out.println("小数数据：" + f);
        } else {
            // 输入错误的信息
            System.out.println("输入的不是小数！");
        }
        
        Scanner scan4 = new Scanner(System.in);
        double sum = 0;
        int m = 0;
        while (scan4.hasNextDouble()) {
            double x = scan4.nextDouble();
            m = m + 1;
            sum = sum + x;
        }
        System.out.println(m + "个数的和为" + sum);
        System.out.println(m + "个数的平均值是" + (sum / m));
        
        // 读取用户名与密码
        Console cons = System.console();
        String username = cons.readLine("User name: ");
        char[] passwd = cons.readPassword("Password: ");
        
        scan.close();
        scan2.close();
        scan3.close();
        scan4.close();
    }
}
