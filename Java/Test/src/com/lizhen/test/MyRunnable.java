package com.lizhen.test;

public class MyRunnable implements Runnable
{
    private volatile boolean active;
    public void run()
    {
        active = true;
        while (active) // ��һ��
        {
            // ����
        }
    }
    public void stop()
    {
        active = false; // �ڶ���
    }
}
