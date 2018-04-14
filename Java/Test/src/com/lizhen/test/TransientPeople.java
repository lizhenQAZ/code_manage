package com.lizhen.test;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

//定义一个需要序列化的类
class People implements Serializable{
	String name; //姓名
    transient Integer age; //年龄
    public People(String name,int age){
        this.name = name;
        this.age = age;
    }
    public String toString(){
        return "姓名 = "+name+" ,年龄 = "+age;
    }
}

public class TransientPeople {
    public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
        People a = new People("李雷",30);
        System.out.println(a); //打印对象的值
        ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("F://Source//code_manage//Java//Test//src//com//lizhen//test//people.txt"));
        os.writeObject(a);//写入文件(序列化)
        os.close();
        ObjectInputStream is = new ObjectInputStream(new FileInputStream("F://Source//code_manage//Java//Test//src//com//lizhen//test//people.txt"));
        a = (People)is.readObject();//将文件数据转换为对象（反序列化）
        System.out.println(a); // 年龄 数据未定义
        is.close();
    }
}
