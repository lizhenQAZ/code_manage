package com.lizhen.test;

public class TestCat
{
    public static void main(String[] args)
    {
        Cat cat=new Cat("Jack","��ɫ");
        cat.eat();
        cat.run();
        cat.sleep();
    }

}

class Animal 
{
    String name;
    
    public Animal(){}//����Ҫд������캯������ȻCat��Ĵ�������
    
    public Animal(String name)
    {
        this.name=name;
    }
    
    void eat()
    {
        System.out.println(name+"���ڳ�");
    }
    
    void run()
    {
        System.out.println(name+"���ڱ���");
    }
    
    void sleep()
    {
        System.out.println(name+"����˯��");
    }
}

class Cat extends Animal
{
    String color;
    public Cat(String name,String color)
    {
        this.name=name;
        this.color=color;
    }
    void eat()
    {
        System.out.println(color+"��"+name+"���ڳ���");
    }
}
