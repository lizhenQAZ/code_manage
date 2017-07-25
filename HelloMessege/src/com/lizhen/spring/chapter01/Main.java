package com.lizhen.spring.chapter01;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanDefinitionReader;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
public class Main {
	public static void main(String[] args) {
		Resource r= new FileSystemResource("helloMessege.xml");
		DefaultListableBeanFactory f= new DefaultListableBeanFactory();
		XmlBeanDefinitionReader reader = new XmlBeanDefinitionReader(f);
		reader.loadBeanDefinitions(r);
		Person person=(Person)f.getBean("person");
		String s= person.sayHello();
		System.out.println("The person is currently saying " +s);
	}
}
