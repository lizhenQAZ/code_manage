package com.lizhen.test;

public class BubbleSort {
/**
 * N������Ҫ������ɣ��ܹ�����N-1������ÿi�˵��������Ϊ(N-i)�Σ����Կ�����˫��ѭ����䣬������ѭ�������ˣ��ڲ����ÿһ�˵�ѭ��������
 * @param args
 */
    public static void main(String[] args) {
        int arr[] = {26,15,29,66,99,88,36,77,111,1,6,8,8};
        for(int i=0;i < arr.length-1;i++) {//���ѭ��������������
            for(int j=0; j< arr.length-i-1;j++) {
                        //�ڲ�ѭ������ÿһ��������ٴ�
                // ��С��ֵ������ǰ��
                if (arr[j]>arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
            System.out.print("��"+(i+1)+"����������");
                                //�о�ÿ�����������
            for(int a=0;a<arr.length;a++) {
                System.out.print(arr[a] + "\t");
            }
            System.out.println("");
        }
        System.out.println("������������");
        for(int a = 0; a < arr.length;a++) {
            System.out.println(arr[a] + "\t");
        }
    }
}
