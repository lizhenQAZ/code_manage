using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_HelloWorld
{
    class Rectangle {
        double width;
        double length;
        public void AcceptDetails()
        {
            width = 10.1;
            length = 6.1;
        }
        public double GetArea() {
            return width * length;
        }
        public void PrintInfo() {
            Console.WriteLine("rectangle's width is {0}",width);
            Console.WriteLine("rectangle's length is {0}", length);
            Console.WriteLine("rectangle's area is {0}", GetArea());
        }
    }
    class ExcuteRectangle
    {
        static void Main(string[] args)
        {
            /* 我的第一个 C# 程序*/
            Rectangle rt = new Rectangle();
            rt.AcceptDetails();
            rt.PrintInfo();
            Console.ReadKey();
        }
    }
}
