package com.lizhen.test;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

//����һ����Ҫ���л�����
class People implements Serializable{
	String name; //����
    transient Integer age; //����
    public People(String name,int age){
        this.name = name;
        this.age = age;
    }
    public String toString(){
        return "���� = "+name+" ,���� = "+age;
    }
}

public class TransientPeople {
    public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
        People a = new People("����",30);
        System.out.println(a); //��ӡ�����ֵ
        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("F://Source//code_manage//Java//Test//src//com//lizhen//test//people.txt"));
        os.writeObject(a);//д���ļ�(���л�)
        os.close();
        ObjectInputStream is = new ObjectInputStream(new FileInputStream("F://Source//code_manage//Java//Test//src//com//lizhen//test//people.txt"));
        a = (People)is.readObject();//���ļ�����ת��Ϊ���󣨷����л���
        System.out.println(a); // ���� ����δ����
        is.close();
    }
}
