package com.lizhen.test;
import java.io.FileReader;

public class ExceptionDetail {
    /**
     * @param args
     */
    public static void main(String[] args) {
        //����쳣1.���ļ�
        FileReader fr=null;
        try {
            fr=new FileReader("d:\\aa.text");
            // �ڳ����쳣�ĵط�������Ĵ���ľͲ�ִ��
            System.out.println("aaa");
        } catch (Exception e) {
            System.out.println("����catch");
            // �ĵ���ȡ�쳣
            // System.exit(-1);
            System.out.println("message="+e.getLocalizedMessage());  //û�б���һ�г���
            e.printStackTrace();   // ��ӡ�����쳣�����ֿ��Ա��������쳣����
        }
        // ������鲻�ܷ���û�з����쳣������ִ��
        // һ����˵������Ҫ�رյ���Դ���ļ������ӣ��ڴ��
        finally
        {
            System.out.println("����finally");
            if(fr!=null);
            {
                try {
                    fr.close();
                } catch (Exception e) {
                    // TODO: handle exception
                    e.printStackTrace();
                }
            }
        }
        System.out.println("OK");
    }
}
