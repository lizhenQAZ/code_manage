// �ļ���: InsufficientFundsException.java
package com.lizhen.test;

//�Զ����쳣�࣬�̳�Exception��
public class InsufficientFundsException extends Exception
{
	//�˴���amount�������浱�����쳣��ȡ��Ǯ�������ʱ����ȱ����Ǯ
	private double amount;
	public InsufficientFundsException(double amount)
	{
		this.amount = amount;
	} 
	public double getAmount()
	{
		return amount;
	}
}
