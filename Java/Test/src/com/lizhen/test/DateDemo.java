package com.lizhen.test;
import java.util.*;
import java.text.*;

public class DateDemo {
   public static void main(String args[]) {
       // ��ʼ�� Date ����
       Date date = new Date();
       SimpleDateFormat ft = new SimpleDateFormat ("E yyyy.MM.dd 'at' hh:mm:ss a zzz");
       Date t; 
       SimpleDateFormat sdf = new SimpleDateFormat ("yyyy-MM-dd"); 
       String input = args.length == 0 ? "1818-11-11" : args[0]; 
       // ����ʱ��
       int year;
       String months[] = {
       "Jan", "Feb", "Mar", "Apr",
       "May", "Jun", "Jul", "Aug",
       "Sep", "Oct", "Nov", "Dec"};
       Calendar c1 = Calendar.getInstance();
       
       // ʹ�� toString() ������ʾ����ʱ��
       System.out.println(date.toString());
       System.out.println("Current Date: " + ft.format(date));
       System.out.printf("%1$s %2$tB %2$td, %2$tY%n", "Due date:", date);
       System.out.printf("%s %tB %<te, %<tY%n", "Due date:", date);
       // c��ʹ��  
       System.out.printf("ȫ�����ں�ʱ����Ϣ��%tc%n",date);          
       // f��ʹ��  
       System.out.printf("��-��-�ո�ʽ��%tF%n",date);  
       // d��ʹ��  
       System.out.printf("��/��/���ʽ��%tD%n",date);  
       // r��ʹ��  
       System.out.printf("HH:MM:SS PM��ʽ��12ʱ�ƣ���%tr%n",date);  
       // t��ʹ��  
       System.out.printf("HH:MM:SS��ʽ��24ʱ�ƣ���%tT%n",date);  
       // R��ʹ��  
       System.out.printf("HH:MM��ʽ��24ʱ�ƣ���%tR",date);
       // b��ʹ�ã��·ݼ��  
       String str=String.format(Locale.US,"Ӣ���·ݼ�ƣ�%tb",date);       
       System.out.println(str);                                                                              
       System.out.printf("�����·ݼ�ƣ�%tb%n",date);  
       // B��ʹ�ã��·�ȫ��  
       str=String.format(Locale.US,"Ӣ���·�ȫ�ƣ�%tB",date);  
       System.out.println(str);  
       System.out.printf("�����·�ȫ�ƣ�%tB%n",date);  
       // a��ʹ�ã����ڼ��  
       str=String.format(Locale.US,"Ӣ�����ڵļ�ƣ�%ta",date);  
       System.out.println(str);  
       // A��ʹ�ã�����ȫ��  
       System.out.printf("�������ڵļ�ƣ�%tA%n",date);  
       // C��ʹ�ã���ǰ��λ  
       System.out.printf("���ǰ��λ���֣�������λǰ�油0����%tC%n",date);  
       // y��ʹ�ã������λ  
       System.out.printf("��ĺ���λ���֣�������λǰ�油0����%ty%n",date);  
       // j��ʹ�ã�һ�������  
       System.out.printf("һ���е�����������ĵڼ��죩��%tj%n",date);  
       // m��ʹ�ã��·�  
       System.out.printf("��λ���ֵ��·ݣ�������λǰ�油0����%tm%n",date);  
       // d��ʹ�ã��գ���λ���������㣩  
       System.out.printf("��λ���ֵ��գ�������λǰ�油0����%td%n",date);  
       // e��ʹ�ã��գ�һλ�����㣩  
       System.out.printf("�·ݵ��գ�ǰ�治��0����%te",date);
       System.out.print(input + " Parses as "); 
       // �����ַ���Ϊʱ��      
       try { 
           t = sdf.parse(input); 
           System.out.println(t); 
       } catch (ParseException e) { 
           System.out.println("Unparseable using " + sdf); 
       }
       // ����
       try { 
           System.out.println(new Date( ) + "\n"); 
           Thread.sleep(1000*3);   // ����3��
           System.out.println(new Date( ) + "\n"); 
       } catch (Exception e) { 
           System.out.println("Got an exception!"); 
       }
       // ����ʱ����
       try {
           long start = System.currentTimeMillis( );
           System.out.println(new Date( ) + "\n");
           Thread.sleep(5*60*10);
           System.out.println(new Date( ) + "\n");
           long end = System.currentTimeMillis( );
           long diff = end - start;
           System.out.println("Difference is : " + diff);
       } catch (Exception e) {
           System.out.println("Got an exception!");
       }
	   // ��ʼ�� Gregorian ����
	   // ʹ�õ�ǰʱ�������
	   // Ĭ��Ϊ����ʱ���ʱ��
       GregorianCalendar gcalendar = new GregorianCalendar();
       // ��ʾ��ǰʱ������ڵ���Ϣ
       System.out.print("Date: ");
       System.out.print(months[gcalendar.get(Calendar.MONTH)]);
       System.out.print(" " + gcalendar.get(Calendar.DATE) + " ");
       System.out.println(year = gcalendar.get(Calendar.YEAR));
       System.out.print("Time: ");
       System.out.print(gcalendar.get(Calendar.HOUR) + ":");
       System.out.print(gcalendar.get(Calendar.MINUTE) + ":");
       System.out.println(gcalendar.get(Calendar.SECOND));
       // ���Ե�ǰ����Ƿ�Ϊ����
       if(gcalendar.isLeapYear(year)) {
          System.out.println("��ǰ���������");
       }
       else {
          System.out.println("��ǰ��ݲ�������");
       }
       // ��������
       c1.set(2017, 1, 1);
       System.out.println(c1.get(Calendar.YEAR)
               +"-"+c1.get(Calendar.MONTH)
               +"-"+c1.get(Calendar.DATE));
       c1.set(2017, 1, 0);
       System.out.println(c1.get(Calendar.YEAR)
               +"-"+c1.get(Calendar.MONTH)
               +"-"+c1.get(Calendar.DATE));
   }
}
