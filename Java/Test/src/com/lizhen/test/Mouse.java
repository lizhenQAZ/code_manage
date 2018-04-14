package com.lizhen.test;

public class Mouse extends Animal { 
    public Mouse(String myName, int myid) { 
        super(myName, myid); 
    } 
    public static void main(String[] args) {
    	Mouse m = new Mouse("haha", 18);
    	m.eat();
    	m.sleep();
    	m.introduction();
    }
}
