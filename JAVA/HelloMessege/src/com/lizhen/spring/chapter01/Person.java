package com.lizhen.spring.chapter01;
public class Person {
		private IHelloMessege helloMessege;

		public IHelloMessege getHelloMessege() {
			return helloMessege;
		}

		public void setHelloMessege(IHelloMessege helloMessege) {
			this.helloMessege = helloMessege;
		}
		public String sayHello() {
			return this.helloMessege.sayHello();
		}
}
