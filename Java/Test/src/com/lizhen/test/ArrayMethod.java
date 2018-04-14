package com.lizhen.test;
import java.util.Arrays;
public class ArrayMethod {
    public static void output(int[] array) {
        if (array != null) {
            for (int i = 0; i < array.length; i++) {
                System.out.print(array[i] + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] array = new int[5];
        // �������
        Arrays.fill(array, 5);
        System.out.println("������飺Arrays.fill(array, 5)��");
        ArrayMethod.output(array);
        // ������ĵ�2�͵�3��Ԫ�ظ�ֵΪ8
        Arrays.fill(array, 2, 4, 8);
        System.out.println("������ĵ�2�͵�3��Ԫ�ظ�ֵΪ8��Arrays.fill(array, 2, 4, 8)��");
        ArrayMethod.output(array);
        int[] array1 = { 7, 8, 3, 2, 12, 6, 3, 5, 4 };
        // ������ĵ�2������6�����������������
        Arrays.sort(array1, 2, 7);
        System.out.println("������ĵ�2������6��Ԫ�ؽ��������������Arrays.sort(array,2,7)��");
        ArrayMethod.output(array1);
        // �����������������
        Arrays.sort(array1);
        System.out.println("�����������������Arrays.sort(array1)��");
        ArrayMethod.output(array1);
        // �Ƚ�����Ԫ���Ƿ����
        System.out.println("�Ƚ�����Ԫ���Ƿ����:Arrays.equals(array, array1):" + "\n" + Arrays.equals(array, array1));
        int[] array2 = array1.clone();
        System.out.println("��¡������Ԫ���Ƿ����:Arrays.equals(array1, array2):" + "\n" + Arrays.equals(array1, array2));
        // ʹ�ö��������㷨����ָ��Ԫ�����ڵ��±꣨����������õģ�����������ȷ��
        Arrays.sort(array1);
        System.out.println("Ԫ��3��array1�е�λ�ã�Arrays.binarySearch(array1, 3)��" + "\n" + Arrays.binarySearch(array1, 3));
        // ��������ھͷ��ظ���
        System.out.println("Ԫ��9��array1�е�λ�ã�Arrays.binarySearch(array1, 9)��" + "\n" + Arrays.binarySearch(array1, 9));
    }
}
