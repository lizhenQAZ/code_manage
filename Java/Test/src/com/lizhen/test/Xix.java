package com.lizhen.test;

public class Xix {
    // ��̬��Ա 
    public static String string="static��Ա";
    // ��ͨ��Ա
    public String string2="��static��Ա";
    // ��̬����
    public static void method(){
        string="sss";
        //string2="sss";���뱨��,��Ϊ��̬��������ֻ�ܵ��þ�̬������̬��Ա
        //method2();
        System.out.println("����static����,static����������޹�");
    }

    // ��ͨ���� 
    public void method2(){
        string ="string1";
        string2="string2";
        method(); //�Ǿ�̬����������Է�����static�����ĵ���
        System.out.println("���Ƿ�static����,�˷��������ָ���Ķ������������������");
    }
    public static void main(String[] args) {
        Xix x=new Xix();
        x.method2();// ���õ�����ͨ���� 
        x.method();// ���õ��þ�̬����
    }
}

