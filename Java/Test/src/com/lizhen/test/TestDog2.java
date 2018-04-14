package com.lizhen.test;

class Animal {
  void eat() {
    System.out.println("animal : eat");
  }
}
	 
class Dog extends Animal {
  void eat() {
    System.out.println("dog : eat");
  }
  void eatTest() {
    this.eat();   // this �����Լ��ķ���
    super.eat();  // super ���ø��෽��
  }
}
	 
public class TestDog2 {
  public static void main(String[] args) {
    Animal a = new Animal();
    a.eat();
    Dog d = new Dog();
    d.eatTest();
  }
}
