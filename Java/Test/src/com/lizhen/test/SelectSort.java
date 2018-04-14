package com.lizhen.test;

public class SelectSort {
    public static void main(String[] args)
    {
        int[] arr={20,60,51,81,285,12,165,51,81,318,186,9,70};
        for(int a:arr)
        {
            System.out.print(a+" ");
        }
        
        System.out.println("\n"+"---------------��С����---------------");
        
        arr=toSmall(arr);
        for(int a:arr)
        {
            System.out.print(a+" ");
        }
        
        System.out.println("\n"+"---------------�Ӵ�С---------------");
        
        arr=toBig(arr);
        for(int a:arr)
        {
            System.out.print(a+" ");
        }
    }
//	    �Ӵ�С
    public static int[] toSmall(int[] arr)
    {
//��������������һ������������������Ϊ���Ķ���û����֮������Ƚϵ���
        for(int i=0;i<arr.length-1;i++)
        {
/*����������û���������������������һ�������бȽ�
 *��k=i+1����Ϊ����һ�����������������û������
 *��ǰ���Ѿ��ź���������ڱȽ�Ҳû������
 */
            for(int k=i+1;k<arr.length;k++)
            {
                if(arr[k]<arr[i])//��������������������
                {
                    int number=arr[i];
                    arr[i]=arr[k];
                    arr[k]=number;
                }//����
            }
        }
        return arr;
    }
//	    ��С����
//��ǰ��һ��
    public static int[] toBig(int[] arr)
    {
        for(int i=0;i<arr.length-1;i++)
        {
            for(int k=i+1;k<arr.length;k++)
            {
                if(arr[k]>arr[i])
                {
                    int number=arr[i];
                    arr[i]=arr[k];
                    arr[k]=number;
                }
            }
        }
        return arr;
    }
}
