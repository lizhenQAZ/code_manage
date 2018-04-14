package com.lizhen.test;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class SerializeDemo
{
   public static void main(String [] args)
   {
      Employee4 e = new Employee4();
      e.name = "Reyan Ali";
      e.address = "Phokka Kuan, Ambehta Peer";
      e.SSN = 11122333;
      e.number = 101;
      try
      {
         FileOutputStream fileOut =
         new FileOutputStream("com/lizhen/test/SerializeDemo.txt");
         ObjectOutputStream out = new ObjectOutputStream(fileOut);
         out.writeObject(e);
         out.close();
         fileOut.close();
         System.out.printf("Serialized data is saved in com/lizhen/test/SerializeDemo.txt");
      }catch(IOException i)
      {
          i.printStackTrace();
      }
   }
}
