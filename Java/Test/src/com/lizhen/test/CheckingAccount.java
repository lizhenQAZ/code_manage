// �ļ���: CheckingAccount.java
package com.lizhen.test;

// ����ģ�������˻�
public class CheckingAccount
{
// balanceΪ��numberΪ����
private double balance;
private int number;

public CheckingAccount(int number)
{
   this.number = number;
}

//��������Ǯ
public void deposit(double amount)
{
   balance += amount;
}

//������ȡǮ
public void withdraw(double amount) throws InsufficientFundsException
{
   if(amount <= balance)
   {
      balance -= amount;
   }
   else
   {
      double needs = amount - balance;
      throw new InsufficientFundsException(needs);
   }
}

//�������������
public double getBalance()
{
   return balance;
}

//���������ؿ���
public int getNumber()
{
   return number;
}
}
