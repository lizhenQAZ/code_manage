package com.lizhen.test;
import java.applet.Applet;
import java.awt.Graphics;
 
public class HelloWorldApplet extends Applet
{
   public void paint (Graphics g)
   {
      g.drawString ("Hello World", 25, 50);
   }
}
