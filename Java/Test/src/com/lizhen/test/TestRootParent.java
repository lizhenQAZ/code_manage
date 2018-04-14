package com.lizhen.test;

public class TestRootParent
{
    public static void main(String[] args)
    {
        A a=new A();
        B b=new B();
        C c=new C();
        D d=new D();
        speak(a);
        speak(b);
        speak(c);
        speak(d);
    }
// instanceof �ؼ��������ڱȽ��������Ƿ���ͬ����ͬ����true����ͬ����false
//���㲻�������Ҫ�Ĳ�����ʲô���͵ģ�������Object�����棬Object���Դ����κ���
    static void speak(Object obj)
    {
        if(obj instanceof A)//��˼�ǣ���������� A �࣬��ô��ִ��һ�����
        {
            A aobj=(A)obj;//����������ת������Ҫǿ��ת��
            aobj.axx();
        }
        else if(obj instanceof B)
        {
            B bobj=(B)obj;
            bobj.bxx();
        }
        else if(obj instanceof C)
        {
            C cobj=(C)obj;
            cobj.cxx();
        }
    }
}

//��������ĸ��࣬���ǵĺ�������ͬ�������� Object �������
class A
{
    void axx()
    {
        System.out.println("Good morning!");
        System.out.println("This is A");
    }
}

class B
{
    void bxx()
    {
        System.out.println("Holle!");
        System.out.println("This is B");        
    }
}

class C
{
    void cxx()
    {
        System.out.println("Look!");
        System.out.println("This is C");        
    }
}

class D
{
    void dxx()
    {
        System.out.println("Oh!Bad!");
        System.out.println("This is D");        
    }
}
