package com.lizhen.test;
import java.util.regex.*;

class Regex{
   public static void main(String args[]){
	  // Pattern
      String content = "I am du from baidu.com.";
      String pattern = ".*baidu.*";
      boolean isMatch = Pattern.matches(pattern, content);
      System.out.println("字符串中是否包含了 'baidu' 子字符串? " + isMatch);
      
      // Matcher
      // 按指定模式在字符串查找
      String line = "This order was placed for QT3000! OK?";
      String patt = "(\\D*)(\\d+)(.*)";
      String replace = "replace";
      StringBuffer sb = new StringBuffer();
      // 创建 Pattern 对象
      Pattern r = Pattern.compile(patt);
      // 现在创建 matcher 对象
      Matcher m = r.matcher(line);
      if (m.find( )) {
         System.out.println("Found value: " + m.group(0) );
         System.out.println("Found value: " + m.group(1) );
         System.out.println("Found value: " + m.group(2) );
         System.out.println("Found value: " + m.group(3) ); 
         System.out.println("start(): " + m.start());
         System.out.println("end(): " + m.end());
         System.out.println("lookingAt(): " + m.lookingAt());
         System.out.println("matches(): " + m.matches());
         m.appendReplacement(sb, replace);
         m.appendTail(sb);
         System.out.println("appendReplacement()+appendTail():" + sb.toString());
         line = m.replaceAll(replace);
         System.out.println("replaceAll(): " + line);
      } else {
         System.out.println("NO MATCH");
      }
      // 判断qq号码是否合法
      checkQQ("0123134");
   }
   public static void checkQQ(String qq) {                                                            
       String reg = "[1-9][0-9]{4,14}";                  
       System.out.println(qq.matches(reg)?"合法qq":"非法qq");                                 
   }
}
