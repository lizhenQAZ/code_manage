package com.lizhen.test;
import java.io.File;

public class CreateDir {
  public static void main(String args[]) {
    String dirname = "F:\\Source\\code_manage\\Java\\Test\\src\\com\\lizhen\\test\\Test\\CreateDir";
    File d = new File(dirname);
    // ���ڴ���Ŀ¼
    d.mkdirs();
  }
}
