package com.lizhen.test;
import java.io.*;

public class TestFileStream {
  public static void main(String args[]){
    try{
      byte bWrite [] = {11,21,3,40,5};
      OutputStream os = new FileOutputStream("com\\lizhen\\test\\fileStreamTest.txt");
      for(int x=0; x < bWrite.length ; x++){
      os.write( bWrite[x] ); // writes the bytes
    }
    os.close();
 
    InputStream is = new FileInputStream("com\\lizhen\\test\\fileStreamTest.txt");
    int size = is.available();
 
    for(int i=0; i< size; i++){
      System.out.print((char)is.read() + "  ");
    }
      is.close();
    }catch(IOException e){
      System.out.print("Exception");
    }  
  }
}
